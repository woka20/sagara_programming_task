from flask_login import UserMixin
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from app import db, login_manager
from flask_wtf import FlaskForm
import bcrypt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return '<User %s>' % self.username

    def set_password(self, password):
        # self.password = generate_password_hash(password)
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(password.encode('utf-8'), salt)
        

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
    

    @classmethod
    def get(cls, user_id):
        """

        :rtype: object
        :type user_id: int
        """
        try:
            return User.query.filter_by(id=user_id).one()
        except NoResultFound:
            return None


# Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# Login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
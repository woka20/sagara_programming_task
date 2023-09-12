from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
import os
from config import get_config

# Load environment variables from .env
load_dotenv()

# from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = get_config()


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'
# csrf = CSRFProtect(app)

from app.user.controller import auth as auth_blueprint 
from app.blog.controller import blog as blog_blueprint


# Register the "auth" and "blog" blueprint
app.register_blueprint(auth_blueprint)
app.register_blueprint(blog_blueprint)

with app.app_context():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

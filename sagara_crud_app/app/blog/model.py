from app import db
from flask_login import UserMixin

class Blog(db.Model, UserMixin):
    __tablename__= 'blog'
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(500), nullable=False, unique=True)
    title= db.Column(db.String(500), nullable=False)
    post = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    

    
    
    def __init__(self, author, title, post):
        self.author = author
        self.title=title
        self.post=post
        
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
       
    
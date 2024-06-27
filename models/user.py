from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    
    id = Column(String(150), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)
    username = Column(String(150), nullable=False)
    email = Column(String(250), nullable=False)
    image_file = Column(String(250), nullable=False, default='default.jpg')
    password = Column(String(250), nullable=False)
    role = Column(Integer, nullable=False)
    posts = relationship('Post', backref='auther', lazy=True)
    user = relationship('User', backref="posts", lazy=True)


    # def __init__(self, username, email, image_file, password, role):
    #     self.username = username
    #     self.email = email
    #     self.image_file = image_file
    #     self.password = password
    #     self.role = role
    
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


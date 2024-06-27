#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), unique=True, nullable=False, default='default.jpg')
    password = Column(String(60), nullable=False)
    posts = relationship('Post', backref='auther', lazy=True) # Post here is refrencing the class Post not the table

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
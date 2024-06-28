#!/usr/bin/python3
""" holds class Post"""
""" holds class Post"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from datetime import datetime


class Post(BaseModel, Base):
    """Representation of a post """
    __tablename__ = 'posts'
    

    title = Column(String(100), nullable=False)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    content = Column(Text, nullable=False)
    user_id = Column(String(150), ForeignKey('users.id'), nullable=False)  # assuming user_id is varchar(150)
    category_id = Column(String(150), ForeignKey('categories.id'), nullable=True)  # assuming category_id is varchar(150)

    # Relationships
    category = relationship('Category', backref='posts', lazy=True)
    user = relationship('User', backref='user_posts', lazy=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    users = relationship("User", backref="post", foreign_keys="User.post_id")
    post_id = Column(ForeignKey('posts.id'), nullable=False)
    user = relationship('User', backref="posts", lazy=True)


    #relationship
    category = relationship('Category', backref='posts', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

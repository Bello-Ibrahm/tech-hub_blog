#!/usr/bin/python3
""" holds class Post"""
""" holds class Post"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship



class Post(BaseModel, Base):
    """Representation of a post """
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False) # user here is refrencing the table name not the class spcially when we refrencing the foriegn key is always referring to the table name
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    
    #relationship
    category = relationship('Category', backref='posts', lazy=True)
    
    def __repr__(self):
        return f'<Category(id={self.id}, name={self.name})>'
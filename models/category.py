#!/usr/bin/python3
""" holds class Category"""
""" holds class Category"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Text, Integer, Boolean

class Category(BaseModel, Base):
    """Representation of a category """
    
    __tablename__ = 'categories'
    name = Column(String(128), nullable=False)
    slug = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    image_file = Column(String(20), unique=True, nullable=False, default='default.jpg')
    meta_title = Column(String(128), nullable=False)
    meta_description = Column(String(128), nullable=False)
    meta_keywords = Column(String(128), nullable=False)
    

    def __repr__(self):
        return f"Category('{self.name}','{self.description}', '{self.meta_title}', '{self.meta_description}', '{self.meta_keywords}')"

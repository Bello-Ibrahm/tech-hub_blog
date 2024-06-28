#!/usr/bin/python3
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

    slug = Column(String(250), nullable=True)  # Updated to match schema
    description = Column(Text, nullable=False)  # Updated to match schema
    image_file = Column(String(250), nullable=False, default='default.jpg')  # Updated length
    meta_title = Column(String(128), nullable=False)
    meta_description = Column(String(128), nullable=False)
    meta_keyword = Column(String(128), nullable=False)  # Updated field name
    navbar_status = Column(Boolean, default=False)  # Added to match schema
    status = Column(Boolean, default=False)  # Added to match schema
    created_by = Column(String(150), nullable=False)  # Added to match schema

    def __repr__(self):
        return f"Category('{self.name}','{self.description}', '{self.meta_title}', '{self.meta_description}', '{self.meta_keyword}')"

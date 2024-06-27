#!/usr/bin/python3
""" holds class Category"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Text, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from slugify import slugify # to handle the slugs


class Category(BaseModel, Base):
    """Representation of a category """
    
    __tablename__ = 'categories'
    name = Column(String(150), nullable=False, unique=True)
    slug = Column(String(250), nullable=False)
    description = Column(Text, nullable=False)
    image = Column(String(250), nullable=True)
    meta_title = Column(String(200), nullable=False)
    meta_description = Column(String(200), nullable=False)
    meta_keyword = Column(String(200), nullable=False)
    navbar_status = Column(Integer, default=0, nullable=False)
    status = Column(Integer, default=0, nullable=False)
    # created_by = Column(String(150), nullable=False)
    created_by = Column(String(150), ForeignKey('users.id'), nullable=False)
    creator = relationship('User', backref='categories')
    
    def __init__(self, *args, **kwargs):
        """initializes category"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """ Set a slug with slugify """
        if name == "slug":
            value = slugify(value)
        super().__setattr__(name, value)
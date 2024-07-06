#!/usr/bin/python3
""" holds class User"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from slugify import slugify # to handle the slugs


class Post(BaseModel, Base):
    """Representation of a post """
    
    __tablename__ = 'posts'
    name = Column(String(150), nullable=False, unique=True)
    slug = Column(String(250), nullable=False)
    description = Column(Text, nullable=False)
    yt_iframe = Column(Text, nullable=True)
    meta_title = Column(String(200), nullable=False)
    meta_description = Column(String(200), nullable=False)
    meta_keyword = Column(String(200), nullable=False)
    status = Column(Integer, default=0, nullable=False)
    category_id = Column(String(150), ForeignKey('categories.id'), nullable=False)
    created_by = Column(String(150), ForeignKey('users.id'), nullable=False)
    creator = relationship('Category', backref='posts', uselist=True)
    
    def __init__(self, *args, **kwargs):
        """initializes category"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """ Set a slug with slugify """
        if name == "slug":
            value = slugify(value)
        super().__setattr__(name, value)

    def __repr__(self):
        return f'<Category(id={self.id}, name={self.name})>'
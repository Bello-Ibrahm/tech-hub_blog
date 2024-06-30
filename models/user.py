#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
import hashlib


class User(BaseModel, Base):
    """Representation of a user """
    
    __tablename__ = 'users'
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    role = Column(Integer, default=0, nullable=False)
    # posts = relationship('Post', backref='author', lazy=True)
    # categories = relationship('Category', backref='author', lazy=True)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = hashlib.md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    def verify_password(self, entered_password):
        entered_md5_hash = hashlib.md5(entered_password.encode()).hexdigest()
        return entered_md5_hash == self.password
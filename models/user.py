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
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(128), nullable=False)
    role = Column(Integer, default=0, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
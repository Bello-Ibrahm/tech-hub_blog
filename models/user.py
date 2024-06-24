#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Representation of a user """
    
    __tablename__ = 'users'
    email = Column(String(150), nullable=False)
    name = Column(String(150), nullable=False)
    role = Column(String(10), nullable=False)
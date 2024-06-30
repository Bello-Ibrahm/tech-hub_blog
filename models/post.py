#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String


class Post(BaseModel, Base):
    """Representation of a post """
    
    __tablename__ = 'posts'
    
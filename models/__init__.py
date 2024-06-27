#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from models.engine.db_storage import DBStorage
from models.user import User
from models.post import Post
from models.category import Category


storage = DBStorage()
storage.reload()
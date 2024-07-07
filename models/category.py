#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Text, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from slugify import slugify # to handle the slugs


#!/usr/bin/python3
""" holds class Post"""
""" holds class Post"""

from models.base_model import BaseModel, Base
import sqlalchemy
<<<<<<< HEAD
from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

=======
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from datetime import datetime
>>>>>>> 43f724e (edits in post.py file)


class Post(BaseModel, Base):
    """Representation of a post """
    __tablename__ = 'posts'
    
<<<<<<< HEAD
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False) # user here is refrencing the table name not the class spcially when we refrencing the foriegn key is always referring to the table name
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    
    #relationship
    category = relationship('Category', backref='posts', lazy=True)
    
=======

    title = Column(String(100), nullable=False)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    content = Column(Text, nullable=False)
    user_id = Column(String(150), ForeignKey('users.id'), nullable=False)  # assuming user_id is varchar(150)
    category_id = Column(String(150), ForeignKey('categories.id'), nullable=True)  # assuming category_id is varchar(150)

    # Relationships
    category = relationship('Category', backref='posts', lazy=True)
    user = relationship('User', backref='user_posts', lazy=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    users = relationship("User", backref="post", foreign_keys="User.post_id")
    post_id = Column(ForeignKey('posts.id'), nullable=False)
    user = relationship('User', backref="posts", lazy=True)


    #relationship
    category = relationship('Category', backref='posts', lazy=True)

>>>>>>> 43f724e (edits in post.py file)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

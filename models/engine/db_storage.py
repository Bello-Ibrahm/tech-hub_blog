#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.category import Category
from models.post import Post
load_dotenv()  # take environment variables from .env.

classes = {"User": User, "Category": Category, "Post": Post}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        TECH_HUB_MYSQL_USER = getenv('TECH_HUB_MYSQL_USER')
        TECH_HUB_MYSQL_PWD = getenv('TECH_HUB_MYSQL_PWD')
        TECH_HUB_MYSQL_HOST = getenv('TECH_HUB_MYSQL_HOST')
        TECH_HUB_MYSQL_DB = getenv('TECH_HUB_MYSQL_DB')
        TECH_HUB_ENV = getenv('TECH_HUB_ENV')
        # uncomment the below line if you are using mysqldb
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
        # self.__engine = create_engine('mariadb+mariadbconnector://{}:{}@{}/{}'.
                                      format(TECH_HUB_MYSQL_USER,
                                             TECH_HUB_MYSQL_PWD,
                                             TECH_HUB_MYSQL_HOST,
                                             TECH_HUB_MYSQL_DB))
        if TECH_HUB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

    def all_vis_cat(self, cls=None):
        """
        Get all the categories from the database
        where navbar_status=0 and status = 0
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss])\
                    .filter(Category.navbar_status == 0, Category.status == 0)\
                    .all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def get_by_email(self, cls, email):
        """
        Returns the object based on the class name and its Email, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.email == email):
                return value
        return None

    def get_by_slug(self, cls, slug):
        """
        Returns the object based on the class name and its slug, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.slug == slug):
                return value
        return None

    def get_posts_with_category(self):
        """
        Fetches all posts along with their associated category.
        Returns a list of tuples (Post object, Category object).
        """
        posts_with_category = []

        posts = self.__session.query(Post).all()
        for post in posts:
            category = self.__session.query(Category)\
                    .filter_by(id=post.category_id).first()
            posts_with_category.append((post, category))

        return posts_with_category

    def get_visible_P_C(self, category_id):
        """
        Fetches all posts along with their associated category
        where category's navbar_status=0 and status=0.
        Returns a list of tuples (Post object, Category object).
        """
        posts_with_category = []

        # Perform a join query to fetch posts and their associated categories
        query = self.__session.query(Post, Category)\
            .join(Category, Post.category_id == Category.id)\
            .filter(Category.navbar_status == 0, Category.status == 0, Post.status == 0, Post.category_id == category_id)\
            .all()

        for post, category in query:
            posts_with_category.append((post, category))

        return posts_with_category

    def postView(self, cat_id, post_id):
        """
        Fetches all posts along with their associated category
        where category's navbar_status=0 and status=0.
        Returns a list of tuples (Post object, Category object).
        """
        posts_with_category = []

        # Perform a join query to fetch posts and their associated categories
        query = self.__session.query(Post, Category)\
            .join(Category, Post.category_id == Category.id)\
            .filter(Post.status == 0, Post.id == post_id, Post.category_id == cat_id)\
            .all()

        for post, category in query:
            posts_with_category.append((post, category))

        return posts_with_category

    def get_posts_with_category_by_category_id(self, category_id):
        """
        Fetches posts associated with a specific category ID
        where category's navbar_status=0 and status=0.
        Returns a list of tuples (Post object, Category object).
        """
        posts_with_category = []

        # Perform a join query to fetch posts and their associated categories
        query = self.__session.query(Post, Category).join(Category, Post.category_id == Category.id)\
            .filter(Category.id == category_id, Category.navbar_status == 0, Category.status == 0).all()

        for post, category in query:
            posts_with_category.append((post, category))

        return posts_with_category

    def update(self, cls, id, **kwargs):
        """
        Update the object based on the class name and its ID
        with the provided kwargs.
        """
        obj = self.get(cls, id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            self.save()  # Commit the changes to the database
            return obj
        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
#from models import storage

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.users import *
<<<<<<< HEAD
from api.v1.views.posts import *
from api.v1.views.categories import *
=======
from api.v1.views.post import *
from api.v1.views.category import *
>>>>>>> 405d5c8 (DB is now connected with the models)

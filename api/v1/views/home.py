#!/usr/bin/python3
"""View for Home Page"""
from flask import render_template
from api.v1.views import app_views
from models import storage
from models.post import Post

@app_views.route('/', strict_slashes=False)
def home():
    """Home page route"""
    posts = storage.all(Post)
    return render_template('home.html', posts=posts)

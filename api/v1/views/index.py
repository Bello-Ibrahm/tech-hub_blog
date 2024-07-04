#!/usr/bin/python3
""" Index """
from models import storage
from api.v1.views import app_views
from flask import jsonify
from .categories import get_categories


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    cats = get_categories()
    data = {
        "users": storage.count("User"),
        # "categories": storage.count("Category"),
        "categories": cats,
        "posts": storage.count("Post"),
    }
    res = jsonify(data)
    res.status_code = 200
    return res

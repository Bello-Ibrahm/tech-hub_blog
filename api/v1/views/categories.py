#!/usr/bin/python3
"""View for Category objects that handles all default RestFul API actions"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models.category import Category
from models import storage

@app_views.route("/categories", strict_slashes=False, methods=['GET'])
def get_categories():
    """Retrieve all categories"""
    category_list = []
    categories = storage.all(Category)
    for c in categories.values():
        category_list.append(c.to_dict())
    return jsonify(category_list)

@app_views.route("/categories/<category_id>", strict_slashes=False, methods=['GET'])
def get_category_id(category_id):
    category = storage.get(Category, category_id)
    if category is None:
        abort(404)
    return jsonify(category.to_dict())

@app_views.route("/categories/<category_id>", strict_slashes=False, methods=['DELETE'])
def del_category(category_id):
    """Deleting a specific category by id"""
    category = storage.get(Category, category_id)
    if category is None:
        abort(404)
    storage.delete(category)
    storage.save()
    print("Category has been deleted successfully")
    return jsonify({}), 200

@app_views.route("/categories", strict_slashes=False, methods=['POST'])
def post_category():
    """Creating a new category"""
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")

    req_fields = ['name', 'slug', 'description', 'image', 'meta_title', 'meta_description', 
                  'meta_keyword', 'navbar_status', 'status', 'created_by', 'creator']
    for field in req_fields:
        if field not in data:
            abort(400, f"Missing {field}")

    # Creating new category 
    new_category = Category(**data)
    new_category.save()
    print("Category has been created successfully")
    return jsonify(new_category.to_dict()), 201

@app_views.route("/categories/<category_id>", strict_slashes=False, methods=['PUT'])
def update_category(category_id):
    """Updating a specific category info"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    updated_category = storage.get(Category, category_id)
    if updated_category is None:
        abort(404)

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(updated_category, key, value)
    storage.save()
    print("Category has been updated successfully")
    return jsonify(updated_category.to_dict()), 200

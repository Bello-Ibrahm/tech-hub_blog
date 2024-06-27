#!/usr/bin/python3
"""View for User objects that handles all default RestFul API actions"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from models import storage
from models.post import Post

@app_views.route("/posts", strict_slashes=False, methods=['GET'])
def get_posts():
  """retreive all posts"""
  post_list = []
  posts = storage.all(Post)
  for p in posts.values():
    post_list.append(p.to_dict())
  return jsonify(post_list)

@app_views.route("/posts/<post_id>", strict_slashes=False, methods=['GET'])
def get_post_id(post_id):
  post = storage.get(Post, post_id)
  if post is None:
    abort(404)
  return jsonify(post.to_dict())

@app_views.route("/post/<post_id>", strict_slashes=False, methods=['DELETE'])
def del_post(post_id):
  """deleting a spcfc post by id"""
  post = storage.get(Post, post_id)
  if post is None:
    abort(404)
  storage.delete(post)
  storage.save()
  print("Post has been deleted successfully")
  return jsonify({}), 200

@app_views.route("/posts", strict_slashes=False, methods=['POST'])
def post_user():
  """Creating a new post"""
  data = request.get_json()
  if not data:
    abort(400, "Not a json")

  req_fields = ['name', 'slug', 'description', 'yt_iframe', 'meta_title', 'meta_description',
                 'meta_keyword', 'status', 'category_id', 'created_by']
  for field in req_fields:
    if field not in data:
      abort(400, description=f"Missing {field}")

  #Creting new user 
  new_post= Post(**data)
  new_post.save()
  print("Post has been created successfully")
  return jsonify(new_post.to_dict()), 201


@app_views.route("/posts/<post_id>", strict_slashes=False, methods=['PUT'])
def update_post(post_id):
  """Updating a specfc Post content"""
  data = request.get_json()
  if not data:
    abort(400, 'Not a JSON')
  updated_post = storage.get(Post, post_id)
  if updated_post is None:
    abort(404)

  for key, value in data.items():
    if key not in ['id', 'created_at', 'updated_at']:
      setattr(updated_post, key, value)
  storage.save()
  print("Post has been updated successfully")
  return jsonify(updated_post.to_dict()), 200

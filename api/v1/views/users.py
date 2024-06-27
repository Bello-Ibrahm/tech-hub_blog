#!/usr/bin/python3
"""View for User objects that handles all default RestFul API actions"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from models import storage

@app_views.route("/users", strict_slashes=False, methods=['GET'])
def get_users():
  """retreive all users"""
  users_list = []
  users = storage.all(User)
  
  # testing purposes
  if not users:
    print("Empty list no users have been created yet")

  for user in users.values():
    users_list.append(user.to_dict())
  return jsonify(users_list)

@app_views.route("/users/<user_id>", strict_slashes=False, methods=['GET'])
def get_user_id(user_id):
  user = storage.get(User, user_id)
  if user is None:
    abort(404)
  return jsonify(user.to_dict())

@app_views.route("/users/<user_id>", strict_slashes=False, methods=['DELETE'])
def del_user(user_id):
  """deleting a spcfc user by id"""
  user = storage.get(User, user_id)
  if user is None:
    abort(404)
  storage.delete(user)
  storage.save()
  print("User has been deleted successfully")
  return jsonify({}), 200

@app_views.route("/users", strict_slashes=False, methods=['POST'])
def create_user():
  """Creating a new user"""
  data = request.get_json()
  if not data:
    abort(400, "Not a json")

  req_fields = ['name', 'email', 'password', 'role']
  for field in req_fields:
    if field not in data:
      abort(400, desc=f"Missing {field}")

  #Creting new user 
  new_user = User(**data)
  new_user.save()
  print("User has been created successfully")
  return jsonify(new_user.to_dict()), 201


@app_views.route("/users/<user_id>", strict_slashes=False, methods=['PUT'])
def update_user(user_id):
  """Updating a specfc user info"""
  data = request.get_json()
  if not data:
    abort(400, 'Not a JSON')
  updated_user = storage.get(User, user_id)
  if updated_user is None:
    abort(404)

  for key, value in data.items():
    if key not in ['id', 'email', 'created_at', 'updated_at']:
      setattr(updated_user, key, value)
  storage.save()
  print("User has been updated successfully")
  return jsonify(updated_user.to_dict()), 200

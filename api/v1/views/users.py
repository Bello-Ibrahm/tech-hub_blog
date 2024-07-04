<<<<<<< HEAD
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
def post_user():
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
=======
# #!/usr/bin/python3
# """View for User objects that handles all default RestFul API actions"""
# from flask import Flask, jsonify, abort, request
# from api.v1.views import app_views
# from models.user import User
# from models import storage


# @app_views.route("/register", methods=["POST"], strict_slashes=False)
# def register_user():
#     data = request.json
#     if not data:
#         return jsonify({"error": "Missing user data"}), 400

#     # Ensure all required fields are present in the incoming data
#     required_fields = ['username', 'email', 'password']
#     for field in required_fields:
#         if field not in data:
#             return jsonify({"error": f"Missing {field} field in JSON"}), 400

#     # Hash the password before storing
#     hashed_password = hash_password(data['password'])  # Implement hash_password function

#     # Create a new User object
#     new_user = User(
#         username=data['username'],
#         email=data['email'],
#         image_file=data.get('image_file', 'default.jpg'),  # Default image if not provided
#         password=hashed_password
#     )
#     print(f'Username: {new_user}')
#     # Save the user to the database
#     storage.new(new_user)
#     storage.save()
    

#     return jsonify(new_user.to_dict()), 201


# # Function to hash the password securely (example using bcrypt)
# def hash_password(password):
#     import bcrypt
#     hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#     return hashed.decode('utf-8')

>>>>>>> 405d5c8 (DB is now connected with the models)

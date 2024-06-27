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


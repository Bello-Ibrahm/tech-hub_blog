#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.user import User
from flask import Flask, jsonify, make_response

app = Flask(__name__)

user_obj = [
    {
        'name': "Mohammad Bello Ibrahim",
        'email': "example@gmail.com",
        'password': "123abc"
    },
    {
        'name': "Asmaa Shihaata",
        'email': "example2@gmail.com",
        'password': "abc123"
    }
]

@app.route('/')
def insert_user():
    for user_data in user_obj:
        # Create a User object using the dictionary
        new_user = User(**user_data)
    
        # Add the new user to the session
        storage.new(new_user)
    
        # Commit the session to the database
        storage.save()
    
    return 'User inserted successfully!'

@app.route('/users', methods=['GET'])
def get_user():
    # Get Users records
    users = storage.all(User).values()
    # users = sorted(users, key=lambda k: k.name)

    if users:
        user_list = [{'name': user.name, 'email': user.email, 'role': user.role} for user in users]
        return make_response(jsonify({'data': user_list}), 200)
    else:
        return make_response(jsonify({'error': "No record found!"}), 404)


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from os import environ
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
def index():
    """ TECH HUB BLOG is alive! """
    return render_template('index.html')


@app.route('/login', strict_slashes=False)
def login():
    """ Handles login """
    return render_template('login.html')


@app.route('/register', strict_slashes=False)
def register():
    """ Handles register """
    return render_template('register.html')


@app.route('/forgot-password', strict_slashes=False)
def forgot_password():
    """ Handles forgot password """
    return render_template('forgot-password.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)

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
@app.route('/home', strict_slashes=False)
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


@app.route('/dashboard', strict_slashes=False)
def dashboard():
    """ Handles admin dashboard """
    return render_template('dashboard.html')


@app.route('/user', strict_slashes=False)
def user():
    """ Handles User """
    return render_template('user.html')


@app.route('/post', strict_slashes=False)
def post():
    """ Handles Post """
    return render_template('post.html')


@app.route('/view-post', strict_slashes=False)
def view_post():
    """ Handles admin view post """
    return render_template('view-post.html')


@app.route('/category', strict_slashes=False)
def category():
    """ Handles Category """
    return render_template('category.html')


@app.route('/view-category', strict_slashes=False)
def view_category():
    """ Handles view Category """
    return render_template('view-category.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)

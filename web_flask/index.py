#!/usr/bin/python3
"""Starts a Flash Web Application"""

import os
from datetime import timedelta
import secrets
from PIL import Image
from flask import (
    Flask, render_template, redirect,
    flash, url_for, request, session
)
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, flash, url_for, request
from .forms import LoginForm, RegistrationForm 
from slugify import slugify # to handle the slugs
from models import storage
from models.category import Category
from models.post import Post
from models.user import User
from sqlalchemy.exc import IntegrityError
from flask_session import Session

load_dotenv()




app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['UPLOAD_FOLDER'] = 'static/images/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}

Session(app)


@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def index():
    """TECH HUB BLOG is alive!"""
    categories = storage.all(Category).values()
    nav_cont_lst = []
    for category in categories:
        if category.navbar_status == 0 and category.status == 0:
            nav_cont_lst.append(category)
    if nav_cont_lst:
        return render_template('index.html', nav_cont_lst=nav_cont_lst)
    return render_template('index.html', title='Home')


@app.route('/tutorial/<string:category_slug>', methods=['POST', 'GET'], strict_slashes=False)
def tutorial(category_slug):
    """ Handle to get all category, post and return both """
    categories = storage.all(Category).values()
    nav_cont_lst = []
    for category in categories:
        if category.navbar_status == 0 and category.status == 0:
            nav_cont_lst.append(category)
    
    cat_slug = storage.get_by_slug(Category, category_slug)
    psts = storage.get_by_slug(Post, category_slug)
    return render_template('tutorial.html', nav_cont_lst=nav_cont_lst, cat_slug=cat_slug, psts=psts)


@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """Handles login"""
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.email.data == 'hello@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'error')

    return render_template('login.html', title='login', form=form)


@app.route('/forgot-password', strict_slashes=False)
def forgot_password():
    """Handles forgot password"""
    return render_template('forgot-password.html', title='Forgot password')


@app.route('/admin/dashboard', strict_slashes=False)
def dashboard():
    """ Handles admin dashboard """
    return render_template('dashboard.html', title='dashboard')


@app.route('/user', strict_slashes=False)
def user():
    """ Handles User """
    return render_template('user.html')


@app.route('/admin/delete-category/<string:category_id>', methods=['GET'])
def delete_category(category_id):
    """Handles view Category"""
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'GET':
            category = storage.get(Category, category_id)
            if category:
                try:
                    import os
                    
                    def remove_current_img(image_path):
                        """Remove the current image"""
                        if os.path.exists(image_path):
                            os.remove(image_path)
                    
                    if category.image:
                        remove_current_img(category.image)
                    # Assuming storage.delete() handles deletion
                    storage.delete(category)
                    storage.save()  # Commit changes to the database
                    flash('Category deleted successfully', 'success') # Handled by the sweetalert
                except Exception as e:
                    flash(f'Error deleting category: {str(e)}', 'error')
            else:
                flash('Category not found!', 'error')
        return redirect(url_for('view_category'))
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/post', methods=['POST', 'GET'], strict_slashes=False)
def post():
    """Handles Post"""
    if session.get('logged_in') and session.get('admin'):
        form = PostForm()
        if form.validate_on_submit() and request.method == "POST":
            name = form.name.data
            category_id = form.category_id.data
            slug = form.slug.data
            description = form.description.data
            yt_iframe = form.yt_iframe.data
            meta_title = form.meta_title.data
            meta_description = form.meta_description.data
            meta_keyword = form.meta_keyword.data
            status = 1 if form.status.data else 0
            created_by = request.form['created_by']

            post = Post(
                name=name,
                category_id=category_id,
                slug=slug,
                description=description,
                yt_iframe=yt_iframe,
                meta_title=meta_title,
                meta_description=meta_description,
                meta_keyword=meta_keyword,
                status=status,
                created_by=created_by
            )

            try:  # To handle Duplicate category name
                storage.new(post)

                # Commit the session to the database
                storage.save()
                flash('Post added successfully', 'success')
                return redirect(url_for('post'))
            except IntegrityError:
                flash('Post name exists. Try another one', 'warning')
                return render_template('post.html', title='Post', form=form)
        return render_template('post.html', title='Post', form=form)
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))

@app.route('/admin/view-post', methods=['GET'], strict_slashes=False)
def view_post():
    """Handles admin view post"""
    if session.get('logged_in') and session.get('admin'):
        posts = storage.get_posts_with_category()
        return render_template('view-post.html', title='View Post', posts=posts)
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))



@app.route('/admin/edit-post/<string:post_id>', methods=['GET'], strict_slashes=False)
def edit_post(post_id):
    """Handles edit Post"""
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'GET':
            post = storage.get(Post, post_id)
            categories = storage.all(Category).values()
            if post and categories:
                return render_template('edit-post.html', title='Edit Post', post=post, categories=categories)
            else:
                flash('No record found', 'warning')
                return redirect(url_for('view_post'))
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/update-post/', methods=['POST'], strict_slashes=False)
def update_post():
    """Handles update post"""
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'POST':
            try:
                category_id = request.form['category_id']
                post_id = request.form['post_id']
                name = request.form['name']
                slug = request.form['slug']
                description = request.form['description']
                yt_iframe = request.form['yt_iframe']
                meta_title = request.form['meta_title']
                meta_description = request.form['meta_description']
                meta_keyword = request.form['meta_keyword']
                status = 1 if request.form.get('status') else 0

                post = storage.update(Post,
                                            post_id,
                                            category_id=category_id,
                                            name=name,
                                            slug=slug,
                                            description=description,
                                            yt_iframe=yt_iframe,
                                            meta_title=meta_title,
                                            meta_description=meta_description,
                                            meta_keyword=meta_keyword,
                                            status=status
                                            )
                storage.new(post)

                # Commit the session to the database
                storage.save()
                flash('Record updated successfully', 'success')

            except IntegrityError:
                flash('Post name exists. Use another one', 'warning')
                storage.reload()
                return redirect(url_for('edit_post', post_id=post_id))

        return redirect(url_for('view_post'))
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/delete-post/<string:post_id>', methods=['GET'])
def delete_post(post_id):
    """Handles delete post"""
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'GET':
            post = storage.get(Post, post_id)
            if post:
                try:
                    # Assuming storage.delete() handles deletion
                    storage.delete(post)
                    storage.save()  # Commit changes to the database
                    flash('Post deleted successfully', 'success') # Handled by the sweetalert
                except Exception as e:
                    flash(f'Error deleting category: {str(e)}', 'error')
            else:
                flash('Post not found!', 'error')
        return redirect(url_for('view_post'))
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))

@app.route('/admin/user', methods=['POST', 'GET'], strict_slashes=False)
def user():
    """Handles User"""
    if session.get('logged_in') and session.get('admin'):
        form = RegistrationForm()
        if form.validate_on_submit() and request.method == "POST":
            name = form.name.data
            email = form.email.data
            password = form.password.data
            role = request.form['role']
            
            try:  # To handle Duplicate email
                new_user = User(name=name, email=email, password=password)
                # Add the new user to the session
                storage.new(new_user)

                # Commit the session to the database
                storage.save()
                flash('Registration successful', 'success')
                return redirect(url_for('view_user'))
            except IntegrityError:
                flash('Email exists.Use a different email.', 'warning')
                return render_template('user.html', form=form)
        return render_template('user.html', title='User', form=form)
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/view-user', strict_slashes=False)
def view_user():
    """Handles User"""
    if session.get('logged_in') and session.get('admin'):
        users = storage.all(User).values()
        users = sorted(users, key=lambda k: k.name)
        return render_template('view-user.html', title='User', users=users)
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/edit-user/<string:user_id>', methods=['POST', 'GET'], strict_slashes=False)
def edit_user(user_id):
    """Handles User"""
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'GET':
            user = storage.get(User, user_id)
            if user:
                return render_template('edit-user.html', title='Edit User', user=user)
            else:
                flash('No user found', 'warning')
                return redirect(url_for('view_user'))
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/update-user/', methods=['POST'], strict_slashes=False)
def update_user():
    """Handles update post"""
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'POST':
            try:
                user_id = request.form['user_id']
                name = request.form['name']
                role = request.form['role']
                user = storage.update(User,
                                            user_id,
                                            name=name,
                                            role=role
                                            )
                storage.new(user)

                # Commit the session to the database
                storage.save()
                flash('Record updated successfully', 'success')

            except IntegrityError:
                flash('User email exists. Use another one', 'warning')
                storage.reload()
                return redirect(url_for('edit_user', user_id=user_id))

        return redirect(url_for('view_user'))
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


if __name__ == "__main__":
    """Main Function"""
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.user import User
from models.category import Category
from models.post import Post
from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, flash, url_for, request, session
from .forms import LoginForm, RegistrationForm, CategoryForm, PostForm
from flask_session import Session
import hashlib
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem' 
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
Session(app)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


# @app.before_request
# def check_session():
#     if request.endpoint and request.endpoint != 'login' and 'logged_in' not in session:
#         flash('Session expired. Please log in again.', 'warning')
#         return redirect(url_for('login'))
#         # return render_template('login.html', form=form)
#     elif 'logged_in' in session:
#         session.modified = True  # Update session timestamp on each request


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def index():
    """ TECH HUB BLOG is alive! """

    return render_template('index.html', title='Home')


@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """ Handles login """
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data

        if remember:
            session.permanent = True
        else:
            session.permanent = False
        user = storage.get_by_email(User, email)
        if user and user.verify_password(password):
            session['logged_in'] = True  
            session['user_id'] = user.id
            session['user_name'] = user.name 
            session['user_email'] = user.email
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to dashboard or home page
        else:
            flash('Invalid email or password', 'error')
            form.password.data = None # Return empty password field
    return render_template('login.html', title='Login', form=form)


@app.route('/logout', methods=['POST', 'GET'], strict_slashes=False)
def logout():
    session.clear()  # Clear all session variables
    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'], strict_slashes=False)
def register():
    """ Handles register """
    form = RegistrationForm()
    if form.validate_on_submit() and request.method == "POST":
        name = form.name.data
        email = form.email.data
        password = form.password.data

        new_user = User(name=name, email=email, password=password)

        try: # To handle Duplicate email
            # Add the new user to the session
            storage.new(new_user)
    
            # Commit the session to the database
            storage.save()
            flash('Regirstration successfully', 'success')
            return redirect(url_for('login'))
        except IntegrityError:
            flash('Email already exists. Please use a different email address.', 'warning')
            return render_template('register.html', form=form)
    return render_template('register.html', title='Register', form=form)


@app.route('/forgot-password', strict_slashes=False)
def forgot_password():
    """ Handles forgot password """
    return render_template('forgot-password.html', title='Forgot password')


@app.route('/dashboard', strict_slashes=False)
def dashboard():
    """ Handles admin dashboard """
    if session.get('logged_in'):
        return render_template('dashboard.html', title='Dashboad')
    else:
        flash('Please login to access the dashboard', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/post', methods=['POST', 'GET'], strict_slashes=False)
def post():
    """ Handles Post """
    # if session.get('logged_in'):
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
        created_by = form.created_by.data

        post = Post(
            name=name,
            category_id=category_id,
            slug=slug,
            description=description,
            yt_iframe=yt_iframe,
            meta_title=meta_title,
            meta_desciption=meta_description,
            meta_keyword=meta_keyword,
            status=status,
            created_by=created_by
        )

        try: # To handle Duplicate category name
            storage.new(category)
    
            # Commit the session to the database
            storage.save()
            flash('Post added successfully', 'success')
            # return redirect(url_for('login'))
        except IntegrityError:
            flash('Post name exists. Try another one', 'warning')
            return render_template('post.html', title='Post', form=form)
    else:
        return render_template('post.html', title='Post', form=form)
    # else:
        # flash('Please login to access the dashboard', 'warning')
        # return redirect(url_for('login'))


@app.route('/admin/view-post', strict_slashes=False)
def view_post():
    """ Handles admin view post """
    if session.get('logged_in'):
        return render_template('view-post.html', title='View Post')
    else:
        flash('Please login to access the dashboard', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/category', methods=['POST', 'GET'], strict_slashes=False)
def category():
    """ Handles Category """
    if session.get('logged_in'):
        form = CategoryForm()
        if form.validate_on_submit() and request.method == "POST":
            name = form.name.data
            slug = form.slug.data
            description = form.description.data
            image = form.image.data
            meta_title = form.meta_title.data
            meta_description = form.meta_description.data
            meta_keyword = form.meta_keyword.data
            navbar_status = 1 if form.navbar_status.data else 0
            status = 1 if form.status.data else 0
            created_by = form.created_by.data

            category = Category(
                name=name,
                slug=slug, 
                description=description,
                image=image,
                meta_title=meta_title,
                meta_description=meta_description,
                meta_keyword=meta_keyword,
                navbar_status=navbar_status,
                status=status,
                created_by=created_by
            )

            try: # To handle Duplicate category name
                storage.new(category)

                # Commit the session to the database
                storage.save()
                flash('Category added successfully', 'success')
                return redirect(url_for('category'))
            except IntegrityError:
                flash('Category name exists. Try another one', 'warning')
                return render_template('category.html', title='Category', form=form)
        return render_template('category.html', title='Category', form=form)
    else:
        flash('Please login to access the dashboard', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/view-category', strict_slashes=False)
def view_category():
    """ Handles view Category """
    if session.get('logged_in'):
        categories = storage.all(Category).values()
        # Sorting categories by name
        categories = sorted(categories, key=lambda k: k.name)

        return render_template('view-category.html', title='View Category', categories=categories)
    else:
        flash('Please login to access the dashboard', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/edit-category/<string:category_id>', methods=['POST', 'GET'], strict_slashes=False)
def edit_category(category_id):
    """ Handles view Category """
    return render_template('edit-category.html', title='Edit Category')


@app.route('/admin/delete-category/<string:category_id>', methods=['GET'])
def delete_category(category_id):
    """ Handles view Category """
    if request.method == 'GET':
        category = storage.get(Category, category_id)
        if category:
            try:
                # Assuming storage.delete() handles deletion
                storage.delete(category)
                storage.save()  # Commit changes to the database
                flash('Category deleted successfully', 'success')
            except Exception as e:
                flash(f'Error deleting category: {str(e)}', 'error')
        else:
            flash('Category not found!', 'error')
    return redirect(url_for('view_category'))



@app.route('/admin/user', strict_slashes=False)
def user():
    """ Handles User """
    if session.get('logged_in'):
        users = storage.all(User).values()
        users = sorted(users, key=lambda k: k.name)
        return render_template('user.html', title='User', users=users)
    else:
        flash('Please login to access the dashboard', 'warning')
        return redirect(url_for('login'))



@app.route('/admin/view-user', strict_slashes=False)
def view_user():
    """ Handles User """
    if session.get('logged_in'):
        users = storage.all(User).values()
        users = sorted(users, key=lambda k: k.name)
        return render_template('user.html', title='User', users=users)
    else:
        flash('Please login to access the dashboard', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/edit-user/<string:user_id>', methods=['POST', 'GET'], strict_slashes=False)
def edit_user(user_id):
    """ Handles User """
    if session.get('logged_in'):
        users = storage.all(User).values()
        users = sorted(users, key=lambda k: k.name)
        return render_template('user.html', title='User', users=users)
    else:
        flash('Please login to access the dashboard', 'warning')
        return redirect(url_for('login'))

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)

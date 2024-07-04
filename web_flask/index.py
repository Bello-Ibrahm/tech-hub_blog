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
from flask_session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from models import storage
from models.user import User
from models.category import Category
from models.post import Post
from .forms import (
    LoginForm, RegistrationForm,
    CategoryForm, PostForm
)

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
    categories = storage.all_vis_cat(Category).values()
    if categories:
        return render_template('index.html', nav_cont_lst=categories)
    return render_template('index.html', title='Home')


@app.route('/tutorial/<string:category_slug>', methods=['POST', 'GET'], strict_slashes=False)
def tutorial(category_slug):
    """ 
    Handle to get all category, post and return both 
    """
    # Get all visible categories
    cats = storage.all_vis_cat(Category).values()

    # Get category by it slug
    c_slug = storage.get_by_slug(Category, category_slug)

    # Get all posts related to category by category_id
    vs = storage.get_visible_P_C(c_slug.id)
    return render_template('tutorial.html', nav_cont_lst=cats, c_slug=c_slug, vs=vs)


@app.route('/tutorial/<string:category_slug>/<string:post_slug>', methods=['POST', 'GET'], strict_slashes=False)
def post_by_category(category_slug, post_slug):
    """ Handle to get all category, post and return both """
    cats = storage.all_vis_cat(Category).values()
    
    # Get category by it slug
    c_slug = storage.get_by_slug(Category, category_slug)
    # Get post by it slug
    p_slug = storage.get_by_slug(Post, post_slug)

    # Get all posts related to category by category_id
    vs = storage.get_visible_P_C(c_slug.id)

    pst = storage.postView(c_slug.id, p_slug.id)
    
    return render_template('post-by-category.html', nav_cont_lst=cats, c_slug=c_slug, vs=vs, pst=pst)


@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    """Handles login"""
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

            if user.role == 1:
                session['admin'] = True
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'error')
            form.password.data = None  # Return empty password field
    return render_template('login.html', title='Login', form=form)


@app.route('/logout', strict_slashes=False)
def logout():
    session.clear()  # Clear all session variables
    return redirect(url_for('index'))


@app.route('/register', methods=['POST', 'GET'], strict_slashes=False)
def register():
    """Handles register"""
    form = RegistrationForm()
    if form.validate_on_submit() and request.method == "POST":
        name = form.name.data
        email = form.email.data
        password = form.password.data

        new_user = User(name=name, email=email, password=password)

        try:  # To handle Duplicate email
            # Add the new user to the session
            storage.new(new_user)

            # Commit the session to the database
            storage.save()
            flash('Registration successful', 'success')
            return redirect(url_for('login'))
        except IntegrityError:
            flash('Email already exists. Please use a different email address.', 'warning')
            return render_template('register.html', form=form)
    return render_template('register.html', title='Register', form=form)


@app.route('/forgot-password', strict_slashes=False)
def forgot_password():
    """Handles forgot password"""
    return render_template('forgot-password.html', title='Forgot password')


@app.route('/admin/dashboard', strict_slashes=False)
def dashboard():
    """Handles admin dashboard"""
    if session.get('logged_in') and session.get('admin'):
        num_cats = storage.count(Category)
        num_users = storage.count(User)
        num_psts = storage.count(Post)

        return render_template('dashboard.html', title='Dashboard', num_cats=num_cats, num_users=num_users, num_psts=num_psts)
    else:
        flash('Access Restricted', 'warning')
        return redirect(url_for('login'))


def save_image(img):
    """
    Save the uploaded image to the server after resizing it to a thumbnail.

    Parameters:
    img (FileStorage): The image file object to be saved. Should be obtained
                       from a Flask file upload.

    Returns:
    str: The filename of the saved image.
    """
    file_rand_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(img.filename)
    img_fn = file_rand_hex + f_ext
    img_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], img_fn)

    image_resize_output = (500, 500)
    image_result = Image.open(img)
    image_result.thumbnail(image_resize_output)

    image_result.save(img_path)

    return img_fn


@app.route('/admin/category', methods=['POST', 'GET'], strict_slashes=False)
def category():
    """Handles Category"""
    if session.get('logged_in') and session.get('admin'):
        form = CategoryForm()
        if form.validate_on_submit() and request.method == "POST":
            if form.image.data:
                image_upload = save_image(form.image.data)

                name = form.name.data
                slug = form.slug.data
                description = form.description.data
                image = image_upload
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
            else:
                name = form.name.data
                slug = form.slug.data
                description = form.description.data
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
                    meta_title=meta_title,
                    meta_description=meta_description,
                    meta_keyword=meta_keyword,
                    navbar_status=navbar_status,
                    status=status,
                    created_by=created_by
                )

            try:  # To handle Duplicate category name
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
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/view-category', methods=['GET'], strict_slashes=False)
def view_category():
    """Handles view Category"""
    if session.get('logged_in') and session.get('admin'):
        categories = storage.all(Category).values()
        # Sorting categories by name
        categories = sorted(categories, key=lambda k: k.name)
        return render_template('view-category.html', title='View Category', categories=categories)
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/edit-category/<string:category_id>', methods=['GET'], strict_slashes=False)
def edit_category(category_id):
    """Handles edit Category"""
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'GET':
            category = storage.get(Category, category_id)
            if category:
                return render_template('edit-category.html', title='Edit Category', category=category)
            else:
                flash('No category found', 'warning')
                return redirect(url_for('view_category'))
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


def is_allowed_file(fn):
    return '.' in fn and fn.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def remove_current_img(img):
    # Remove current image if it exists
    current_image_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], img)
    # try:
    if os.path.exists(current_image_path):
        os.remove(current_image_path)
        # return True
    # else:
    #     return False  # Image doesn't exist
    # except Exception as e:
        # flash(f'Error deleting current image: {str(e)}', 'warning')
        # return False


@app.route('/admin/update-category/', methods=['POST'], strict_slashes=False)
def update_category():
    """Handles update Category"""
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'POST':
            try:
                # Handle file upload
                if 'image' in request.files:
                    image_file = request.files['image']
                    if image_file.filename != '':
                        if not is_allowed_file(image_file.filename):
                            flash('Only JPEG, PNG, or JPG files allowed.', 'warning')
                            return redirect(url_for('edit_category', category_id=request.form['category_id']))

                        image_upload = save_image(image_file)

                        category_id = request.form['category_id']
                        name = request.form['name']
                        slug = request.form['slug']
                        description = request.form['description']
                        image = image_upload
                        meta_title = request.form['meta_title']
                        meta_description = request.form['meta_description']
                        meta_keyword = request.form['meta_keyword']
                        navbar_status = 1 if 'navbar_status' in request.form else 0
                        status = 1 if request.form.get('status') else 0

                        category = storage.update(Category,
                                                  category_id,
                                                  name=name,
                                                  slug=slug,
                                                  description=description,
                                                  image=image_upload,
                                                  meta_title=meta_title,
                                                  meta_description=meta_description,
                                                  meta_keyword=meta_keyword,
                                                  navbar_status=navbar_status,
                                                  status=status,
                                                  category_id=category_id
                                                  )
                    else:
                        category_id = request.form['category_id']
                        name = request.form['name']
                        slug = request.form['slug']
                        description = request.form['description']
                        meta_title = request.form['meta_title']
                        meta_description = request.form['meta_description']
                        meta_keyword = request.form['meta_keyword']
                        navbar_status = 1 if 'navbar_status' in request.form else 0
                        status = 1 if request.form.get('status') else 0

                        category = storage.update(Category,
                                                  category_id,
                                                  name=name,
                                                  slug=slug,
                                                  description=description,
                                                  meta_title=meta_title,
                                                  meta_description=meta_description,
                                                  meta_keyword=meta_keyword,
                                                  navbar_status=navbar_status,
                                                  status=status,
                                                  category_id=category_id
                                                  )

                        storage.new(category)

                        # Commit the session to the database
                        storage.save()
                        flash('Record updated successfully', 'success')

            except IntegrityError:
                flash('Category name exists. Use another one', 'warning')
                storage.reload()
                return redirect(url_for('edit_category', category_id=category_id))

        return redirect(url_for('view_category'))
    else:
        flash('Access restricted', 'warning')
        return redirect(url_for('login'))


@app.route('/admin/delete-category/<string:category_id>', methods=['GET'])
def delete_category(category_id):
    """Handles view Category"""
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'GET':
            category = storage.get(Category, category_id)
            if category:
                try:
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

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from models import storage
from models.category import Category


class RegistrationForm(FlaskForm):
  name = StringField('Full Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  terms_agreement=BooleanField('I agree to the terms')
  submit = SubmitField('Register')


class LoginForm(FlaskForm):
  email=StringField('Email', validators=[DataRequired(), Email()])
  password=StringField('Password', validators=[DataRequired()])
  remember=BooleanField('Remember Me')
  submit=SubmitField('Login')


class CategoryForm(FlaskForm):
  name = StringField('* Category Name', validators=[DataRequired()])
  slug = StringField('* Slug', validators=[DataRequired()])
  description = TextAreaField('* Description', validators=[DataRequired()])
  image = StringField('Image')
  meta_title = StringField('* Meta Title', validators=[DataRequired()])
  meta_description = StringField('* Meta Description', validators=[DataRequired()])
  meta_keyword = StringField('* Meta Keyword', validators=[DataRequired()])
  navbar_status = BooleanField('Navbar Status')
  status = BooleanField('Status')
  created_by = StringField('created_by', validators=[DataRequired()])
  submit = SubmitField('Save Category')


class PostForm(FlaskForm):
  categories = storage.all(Category).values()

  category_id = SelectField('* Category',
                              choices=[('', '-- Select category --')] + [(category.id, category.name) for category in categories],
                              validators=[DataRequired()])
  name = StringField('* Post Name', validators=[DataRequired()])
  slug = StringField('* Slug', validators=[DataRequired()])
  description = TextAreaField('* Description', validators=[DataRequired()])
  yt_iframe = StringField('Youtube Iframe Link')
  meta_title = StringField('* Meta Title', validators=[DataRequired()])
  meta_description = StringField('* Meta Description', validators=[DataRequired()])
  meta_keyword = StringField('* Meta Keyword', validators=[DataRequired()])
  status = BooleanField('Status')
  created_by = StringField('created_by', validators=[DataRequired()])
  submit = SubmitField('Save Post')
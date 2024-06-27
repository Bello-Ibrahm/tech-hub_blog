from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from models import storage
from models.category import Category


class RegistrationForm(FlaskForm):
  name = StringField('Full Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  terms_agreement=BooleanField('I agree to the terms', validators=[DataRequired()])
  submit = SubmitField('Register')


class LoginForm(FlaskForm):
  email=StringField('Email', validators=[DataRequired(), Email()])
  password=PasswordField('Password', validators=[DataRequired()])
  remember=BooleanField('Remember Me')
<<<<<<< HEAD
  submit=SubmitField('Login')
=======
  submit=SubmitField('Login')
>>>>>>> 80d9713 (DB is now connected with the models)

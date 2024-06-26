from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

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
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length,EqualTo,ValidationError,Email
from wtforms import StringField, PasswordField,SubmitField
from .database import User


class RegisterForm(FlaskForm):

    # when it is used to product from input twice ,give error(to product from same input)
    # Custom check if username is already taken
    # important 'validate' must be included,even function,include validate eg validate_username
    def validate_username(self, check_username):

        # (Username=check_username.data)is important similar in the route.py
        # in this file,when the client take input(must be included .data)
        # in route.py,form.username.data = in database.py,check_username.data
        # they are similar input
        user = User.query.filter_by(Username=check_username.data).first()
        if user:
            raise ValidationError("Username already exists and plz use other name ")

    # Custom check if email is already taken
    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email already exists and plz use other email ")

    username = StringField('Username', validators=[Length(min=2, max=20),DataRequired()])
    email=StringField('Email', validators=[Email(),Length(min=6, max=35),DataRequired()])
    password= PasswordField('Password', validators=[Length(min=6,max=10),DataRequired()])
    confirm_password=PasswordField('Confirm Password', validators=[Length(min=6,max=10),EqualTo('password'),DataRequired()])
    submit = SubmitField('Register')



class LoginForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Length(min=6, max=35)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

from flask import render_template, flash, Blueprint, redirect, url_for
from .register import LoginForm, RegisterForm
from .database import User
from  . import db
from datetime import datetime


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(Username=form.username.data,
                    passwords=form.password.data,
                    email=form.email.data,
                    CreateDate=datetime.utcnow())
        db.session.add(user)
        db.session.commit()
        return render_template("home.html")

    if form.errors!={}:#if there are not errors in form validation
        for error in form.errors.values():
            flash(f"There are error with creating a user :: {error}")
    return render_template('register.html',form=form,category='danger')

@main.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = User.query.filter_by(email=login_form.email.data).first()
        password = User.query.filter_by(password=login_form.password.data).first()
        if email and password:
            return render_template("home.html")
        else:
            flash("Invalid email or password Or create an account")
    return render_template('login.html', login_form=login_form)

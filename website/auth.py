from flask import Blueprint, session, redirect, url_for, render_template, flash
from .forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, login_required, logout_user
from . import db

authbp = Blueprint('authentication', __name__)

@authbp.route('/login', methods=['GET', 'POST'])
def login():
    login_form_instance = LoginForm()
    error = None

    if (login_form_instance.validate_on_submit() == True):
        # Retrieve submitted username and password from the database
        user_name = login_form_instance.user_name.data
        password = login_form_instance.password.data
        u1 = User.query.filter_by(name=user_name).first()

        # If user is not found within the database
        if u1 is None:
            error = 'Incorrect Username or Password'
        # Check the password
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect Username or Password'
        if error is None:
            login_user(u1)
            return render_template('admin.html')
        else:
            flash(error, 'danger')
    return render_template('login.html', form=login_form_instance, heading='Login')

@authbp.route('/register', methods=['GET', 'POST'])
def register():
    register_form_instance = RegisterForm()

    if (register_form_instance.validate_on_submit() == True):
        # Retrieve information from the Form
        uname = register_form_instance.user_name.data
        pwd = register_form_instance.password.data
        email = register_form_instance.email.data

        # Check if the user exists
        u1 = User.query.filter_by(name=uname).first()
        if u1:
            flash('This username already exists, please attempt login!', 'danger')
            return redirect(url_for('authentication.login'))

        pwd_hash = generate_password_hash(pwd)
        # Create a new user
        new_user = User(name=uname, password_hash=pwd_hash, email_id=email)
        db.session.add(new_user)
        db.session.commit()

        flash('Account successfully created! Please login.', 'success')
        return redirect(url_for('main.admin'))
    else:
        return render_template('register.html', form=register_form_instance, heading='Register')
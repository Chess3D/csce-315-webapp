# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from .services import verify_account
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('/auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Incorrect email or password')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=True)
    return redirect(url_for('main.index'))


@auth.route('/sign-up')
def signup():
    return render_template('auth/signup.html')


@auth.route('/sign-up', methods=['POST'])
def signup_post():
    
    email = request.form.get('email')
    riotID = request.form.get('riotID')
    tagline = request.form.get('tagline')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    if not verify_account(riotID, tagline):
        flash('Invalid RiotID and tagline')
        return redirect(url_for('auth.signup'))

    if (password1 != password2):
        flash('Passwords do not match')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, riotID=riotID, tagline=tagline, password=generate_password_hash(password1, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
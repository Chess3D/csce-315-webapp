# user.py

from flask import Blueprint, render_template
from .models import User

user = Blueprint('user', __name__)


# @user.route('/user')
# def about():
    

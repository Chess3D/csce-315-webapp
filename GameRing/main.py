# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


# HOME
@main.route('/')
def index():
    return render_template('index.html')


# SCRIMS
@main.route('/scrims')
def scrims():
    return render_template('scrims/scrims.html')


# # USER
# @main.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', name=current_user.name)
# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


# HOME
@main.route('/')
def index():
    return render_template('index.html')
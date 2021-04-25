import os
os.environ.setdefault("FLASK_APP", "GameRing")

from flask import Flask
app = Flask(__name__)
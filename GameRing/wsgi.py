import os
from . import app as application

os.environ.setdefault("FLASK_APP", "GameRing")

app = application
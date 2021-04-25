import os
from . import create_app

os.environ.setdefault("FLASK_APP", "GameRing")

app = create_app()

if __name__ == "__main__":
    app.run()
# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'password'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    # AUTH
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # MAIN
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # USER
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    # TEAM
    from .team import team as team_blueprint
    app.register_blueprint(team_blueprint)

    # TOURNAMENT
    from .tournament import tournament as tournament_blueprint
    app.register_blueprint(tournament_blueprint)


    return app

app = create_app()
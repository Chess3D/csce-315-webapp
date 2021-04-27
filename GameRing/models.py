# models.py

from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)

    riotID = db.Column(db.String(100))
    tagline = db.Column(db.String(5))

    password = db.Column(db.String(100))

    is_captian = db.Column(db.Boolean(), default=False)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    players = db.relationship('User', backref='team', lazy=True)

    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))


class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    game_type = db.Column(db.String(100))
    grand_finals_modifier = db.Column(db.String(100))
    url = db.Column(db.String(255), default='coolmathgames.com')
    signup_cap = db.Column(db.Integer)
    start_at = db.Column(db.String(100))
    hold_third_place_match = db.Column(db.Boolean, default=False)
    show_rounds = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(255))
    creator = db.Column(db.String(150), default="Jim")
    teams = db.relationship('Team', backref='tournament', lazy=True)

    
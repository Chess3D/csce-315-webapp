# models.py

from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    players = db.relationship('User', backref='team', lazy=True)

    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))


class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    
    teams = db.relationship('Team', backref='tournament', lazy=True)
    
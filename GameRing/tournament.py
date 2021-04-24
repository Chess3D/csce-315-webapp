# tournament.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User, Tournament, Team
from . import db

tournament = Blueprint('tournament', __name__)


# HOME
@tournament.route('/tournaments')
def tournaments():
    all_tournaments = Tournament.query.all()

    in_tournament = False
    my_tournament = None
    
    if current_user.team_id:
        my_team = Team.query.get(current_user.team_id)

        if my_team.tournament_id:
            my_tournament = Tournament.query.get(my_team.tournament_id)
            in_tournament = True

    return render_template('tournaments/tournaments.html', tournaments=all_tournaments, my_tournament=my_tournament, in_tournament=in_tournament)


# SEARCH
@tournament.route('/tournaments/search', methods=['POST'])
def search():
    search = request.form.get('search')
    tournaments = Tournament.query.filter(Tournament.name.ilike(f'%{search}%'))

    return render_template('tournaments/search.html', tournaments=tournaments)


# CREATE
@tournament.route('/tournaments/create')
def create():
    return render_template('/tournaments/create.html')


@tournament.route('/tournaments/create', methods=['POST'])
def create_post():
    name = request.form.get('name')

    if Tournament.query.filter_by(name=name).first(): 
        flash('Tournament already exists')
        return redirect(url_for('tournament.create'))

    
    tournament = Tournament()
    tournament.name = name

    db.session.add(tournament)
    db.session.commit()

    return redirect(url_for('tournament.tournaments'))



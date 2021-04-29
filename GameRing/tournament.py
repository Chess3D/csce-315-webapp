# tournament.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User, Tournament, Team
from . import db
from datetime import datetime

from .services import create_tournament as challonge_create

tournament = Blueprint('tournament', __name__)


# HOME
@tournament.route('/tournaments')
def tournaments():
    all_tournaments = Tournament.query.all()

    in_tournament = False
    my_tournament = None

    if current_user.is_authenticated and current_user.team_id:
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


# ABOUT
@tournament.route('/tournaments/<string:tournamentID>')
def about(tournamentID):
    this_tournament = Tournament.query.get(tournamentID)

    on_team = False
    in_tournament = False

    current_tournament = False
    payment = False

    if current_user.is_authenticated and current_user.team_id:
        team = Team.query.get(current_user.team_id)
        on_team = True

        if team.tournament_id:
            in_tournament = True
            current_tournament = (team.tournament_id == this_tournament.id)

    return render_template('tournaments/about.html', tournament=this_tournament, in_tournament=in_tournament, current_tournament=current_tournament, on_team=on_team)


@tournament.route('/tournaments/<string:tournamentID>', methods=['POST'])
@login_required
def about_post(tournamentID):
    on_team = False
    in_tournament = False

    team = None

    if current_user.is_authenticated and current_user.team_id:
        on_team = True
        team = Team.query.get(current_user.team_id)

        if team.tournament_id:
            in_tournament = True

    if on_team:
        if not in_tournament:
            team.tournament_id = tournamentID
        else:
            team.tournament_id = None

        db.session.commit()

    return redirect(url_for('tournament.tournaments'))


# CREATE
@tournament.route('/tournaments/create')
def create():
    return render_template('/tournaments/create.html')


@tournament.route('/tournaments/create', methods=['POST'])
def create_post():
    name = request.form.get('name')
    tournament_type = request.form.get('tournament_type')
    grand_finals_modifier = request.form.get('grand_finals_modifier')
    signup_cap = request.form.get('signup_cap')
    description = request.form.get('description')

    settings = {
        'name' : name,
        'url' : None,
        'game_name' : 'League of Legends',
        'tournament_type' : tournament_type,
        'grand_finals_modifier' : grand_finals_modifier,
        'signup_cap' : signup_cap,
        'description' : description,
    }

    if Tournament.query.filter_by(name=name).first():
        flash('Tournament "{name}" already exists')
        return redirect(url_for('tournament.create'))

    if int(signup_cap) < 2:
        flash('Invalid signup capcity')
        return redirect(url_for('tournament.create'))

    # Format the start time
    start_date = request.form.get('start_date')
    start_time = request.form.get('start_time')
    
    start_time_str = f'{start_date} {start_time}'
    start_at = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')

    if start_at < datetime.now():
        flash('Invalid start time')
        return redirect(url_for('tournament.create'))

    entry_fee = request.form.get('entry_fee')

    if Tournament.query.filter_by(name=name).first(): 
        flash('Tournament already exists')
        return redirect(url_for('tournament.create'))

    # Add tournament to challonge
    challonge_id = challonge_create(**settings)

    # Add tournament to database
    tournament = Tournament()
    tournament.challonge_id = challonge_id
    tournament.name = name
    tournament.entry_fee = entry_fee
    tournament.tournament_type = tournament_type
    tournament.signup_cap = signup_cap

    tournament.start_at = start_at
    
    tournament.description = description

    db.session.add(tournament)
    db.session.commit()




    return redirect(url_for('tournament.tournaments'))


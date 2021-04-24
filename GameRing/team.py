# team.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User, Tournament, Team
from . import db

team = Blueprint('team', __name__)


# HOME
@team.route('/team')
def teams():
    all_teams = Team.query.all()

    in_team = False
    my_team = None

    if current_user.is_authenticated and current_user.team_id:
        my_team = Team.query.get(current_user.team_id)
        in_team = True

    return render_template('teams/teams.html', teams=all_teams, my_team=my_team, in_team=in_team)


# SEARCH
@team.route('/team/search', methods=['POST'])
def search():
    search = request.form.get('search')
    teams = Team.query.filter(Team.name.ilike(f'%{search}%'))

    return render_template('teams/search.html', teams=teams)


# ABOUT
@team.route('/team/<string:teamID>')
def about(teamID):
    this_team = Team.query.get(teamID)
    on_team = False

    current_team = False

    if current_user.is_authenticated and current_user.team_id:
        on_team = True
        current_team = (current_user.team_id == this_team.id)
        print(current_team)

    return render_template('teams/about.html', team=this_team, on_team=on_team, current_team=current_team)


@team.route('/team/<string:teamID>', methods=['POST'])
@login_required
def about_post(teamID):
    on_team = False

    if current_user.is_authenticated and current_user.team_id:
        on_team = True

    if not on_team:
        current_user.team_id = teamID
    else:
        current_user.team_id = None

    db.session.commit()


    return redirect(url_for('team.teams'))


# CREATE
@team.route('/team/create')
@login_required
def create():
    return render_template('teams/create.html')


@team.route('/team/create', methods=['POST'])
@login_required
def create_post():
    name = request.form.get('name')

    if Team.query.filter_by(name=name).first(): 
        flash('Team already exists')
        return redirect(url_for('team.create'))

    
    team = Team()
    team.name = name

    db.session.add(team)
    db.session.commit()

    return redirect(url_for('team.teams'))
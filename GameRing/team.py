# team.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User, Tournament, Team
from . import db

team = Blueprint('team', __name__)


# HOME
@team.route('/teams')
def teams():
    all_teams = Team.query.all()

    in_team = False
    my_team = None

    if current_user.is_authenticated and current_user.team_id:
        my_team = Team.query.get(current_user.team_id)
        in_team = True

    return render_template('teams/teams.html', teams=all_teams, my_team=my_team, in_team=in_team)


# SEARCH
@team.route('/teams/search', methods=['POST'])
def search():
    search = request.form.get('search')
    teams = Team.query.filter(Team.name.ilike(f'%{search}%'))

    return render_template('teams/search.html', teams=teams)


# ABOUT
@team.route('/teams/<string:teamID>')
def about(teamID):
    this_team = Team.query.get(teamID)
    on_team = False

    current_team = False

    if current_user.is_authenticated and current_user.team_id:
        on_team = True
        current_team = (current_user.team_id == this_team.id)

    return render_template('teams/about.html', team=this_team, on_team=on_team, current_team=current_team)


@team.route('/teams/<string:teamID>', methods=['POST'])
@login_required
def about_post(teamID):
    on_team = False

    # Currently on the viewed team
    if current_user.is_authenticated and current_user.team_id:
        on_team = True

    # Join team
    if not on_team:
        current_user.team_id = teamID

    # Leave team
    else:
        team = Team.query.get(teamID)

        # Current player is only player
        if len(team.players) == 1:
            flash(f'Team "{team.name}" has been removed')
            db.session.delete(team)
        else:
            for player in team.players:
                if not player.is_captian:
                    User.query.get(player.id).is_captian = True
                    break
       
        current_user.is_captian = False
        current_user.team_id = None

    db.session.commit()


    return redirect(url_for('team.teams'))


# CREATE
@team.route('/teams/create')
@login_required
def create():
    if not current_user.is_authenticated:
        flash('Must be logged in')
        return redirect(url_for('team.teams'))

    if current_user.team_id:
        flash('Cannot create a team while on a team')
        return redirect(url_for('team.teams'))

    return render_template('teams/create.html')


@team.route('/teams/create', methods=['POST'])
@login_required
def create_post():
    name = request.form.get('name')

    if not current_user.is_authenticated:
        flash('Must be logged in')
        return redirect(url_for('team.teams'))

    if current_user.team_id:
        flash('Cannot create a team while on a team')
        return redirect(url_for('team.teams'))

    if Team.query.filter_by(name=name).first(): 
        flash('Team already exists')
        return redirect(url_for('team.create'))

    
    team = Team()
    team.name = name

    db.session.add(team)
    db.session.commit()

    current_user.team_id = team.id
    current_user.is_captian = True
    db.session.commit()

    return redirect(url_for('team.teams'))
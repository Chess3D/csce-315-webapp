# tournament.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User, Tournament, Team
from . import db
from datetime import datetime

from . import services

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

    if this_tournament == None:
        return redirect(url_for('tournament.tournaments'))

    on_team = False
    in_tournament = False

    current_tournament = False
    payment = False

    if not this_tournament.is_active:
        if datetime.now() > this_tournament.start_at:
            if len(this_tournament.teams) > 1:
                services.start_tournament(this_tournament.url)
                this_tournament.is_active = True
                db.session.commit()

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
    tournament = Tournament.query.get(tournamentID)

    value = request.form.get('action')

    if current_user.is_authenticated and current_user.team_id:
        on_team = True
        team = Team.query.get(current_user.team_id)

        if team.tournament_id:
            in_tournament = True

    if on_team:
        if not in_tournament:

            # Join the tournament
            if value == 'Join' and datetime.now() < tournament.start_at:
                if tournament.entry_fee > 0:
                    return redirect(url_for('pay.checkout', tournament=tournament.id, team=team.id, entry_fee=tournament.entry_fee))

                team.tournament_id = tournamentID
                team.participant_id = services.add_participant(tournament.url, team.name)["id"]
            elif value == 'Join':
                flash(f'Unable to join, tournament has already started')

        # Leave the tournamnet
        elif value == 'Leave':
            team.tournament_id = None
            services.remove_participant(tournament.url, team.participant_id)
            team.participant_id = None

        # Report the outcome of the match
        elif value == 'Report Match':
            return redirect(url_for('tournament.report'))

        # Save to database
        db.session.commit()

    return redirect(url_for('tournament.tournaments'))


# REPORT MATCH
@login_required
@tournament.route('/tournaments/report')
def report():
    tournament = None

    match_id = None

    team_temp = None
    team_1 = None
    team_2 = None

    if current_user.team_id:
        team_temp = Team.query.get(current_user.team_id)

        if team_temp.tournament_id:
            tournament = Tournament.query.get(team_temp.tournament_id)
        else:
            flash('Must be in tournament to report match')
            return redirect(url_for('tournaments.tournaments'))
    else:
        flash('Must be on a team to report a match')
        return redirect(url_for('teams.teams'))

    # Determin team_1 and team_2
    for match in services.get_matches(tournament.url):
        match_id = match['id']

        if match['state'] == 'complete':
            continue

        if team_temp.participant_id == match['player1_id']:
            team_1 = team_temp
            team_2 = Team.query.filter_by(participant_id=match['player2_id'], tournament_id=tournament.id).first()
            break
        elif team_temp.participant_id == match['player2_id']:
            team_1 = Team.query.filter_by(participant_id=match['player1_id'], tournament_id=tournament.id).first()
            team_2 = team_temp
            break
    
    try:
        team_1.name
        team_2.name
    except:
        flash('Cannot report this match')
        return redirect(url_for('tournament.about', tournamentID=tournament.id))

    return render_template('tournaments/report.html', team_1=team_1, team_2=team_2)


@login_required
@tournament.route('/tournaments/report', methods=['POST'])
def report_post():
    score_1 = request.form.get('score1')
    score_2 = request.form.get('score2')

    tournament = None

    match_id = None

    team_temp = None
    team_1 = None
    team_2 = None

    if current_user.team_id:
        team_temp = Team.query.get(current_user.team_id)

        if team_temp.tournament_id:
            tournament = Tournament.query.get(team_temp.tournament_id)
        else:
            flash('Must be in tournament to report match')
            return redirect(url_for('tournaments.tournaments'))
    else:
        flash('Must be on a team to report a match')
        return redirect(url_for('teams.teams'))

    # Determine team_1 and team_2
    for match in services.get_matches(tournament.url):
        match_id = match['id']

        if match['state'] == 'complete':
            continue

        if team_temp.participant_id == match['player1_id']:
            team_1 = team_temp
            team_2 = Team.query.filter_by(participant_id=match['player2_id'], tournament_id=tournament.id).first()
            break
        elif team_temp.participant_id == match['player2_id']:
            team_1 = Team.query.filter_by(participant_id=match['player1_id'], tournament_id=tournament.id).first()
            team_2 = team_temp
            break
    
    if int(score_1) > int(score_2):
        param = {'scores_csv' : f'{score_1}-{score_2}', 'winner_id' : team_1.participant_id}
    else:
        param = {'scores_csv' : f'{score_1}-{score_2}', 'winner_id' : team_2.participant_id}

    if param != None:
        services.update_match(tournament.url, match_id, **param)
    
    return redirect(url_for('tournament.about', tournamentID=tournament.id))


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

    if name == '':
        flash('Must input name')
        return redirect(url_for('tournament.create'))

    if tournament_type == 'Choose...':
        flash('Must select elimination type')

    if grand_finals_modifier == 'Choose...':
        flash('Must select grand finals modifier')

    if signup_cap == '':
        flash('Must input sign up capacity')
        return redirect(url_for('tournament.create'))

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
        flash(f'Tournament "{name}" already exists')
        return redirect(url_for('tournament.create'))

    if int(signup_cap) < 4:
        flash('Invalid signup capcity')
        return redirect(url_for('tournament.create'))

    # Format the start time
    start_date = request.form.get('start_date')
    start_time = request.form.get('start_time')

    if start_date == '':
        flash('Must input start date')
        return redirect(url_for('tournament.create'))
    
    if start_time == '':
        flash('Must input start time')
        return redirect(url_for('tournament.create'))
    
    start_time_str = f'{start_date} {start_time}'
    start_at = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')

    if start_at < datetime.now():
        flash('Start time must be in the future')
        return redirect(url_for('tournament.create'))

    entry_fee = request.form.get('entry_fee')

    if entry_fee == '':
        flash('Must input entry fee')
        return redirect(url_for('tournament.create'))

    if Tournament.query.filter_by(name=name).first(): 
        flash('Tournament already exists')
        return redirect(url_for('tournament.create'))

    # Add tournament to challonge
    challonge_id = services.create_tournament(**settings)['id']
    challonge_url = services.get_tournament(challonge_id)['url']

    # Add tournament to database
    tournament = Tournament()
    tournament.challonge_id = challonge_id
    tournament.name = name
    tournament.entry_fee = entry_fee
    tournament.tournament_type = tournament_type
    tournament.signup_cap = signup_cap
    tournament.url = challonge_url

    tournament.start_at = start_at
    
    tournament.description = description

    db.session.add(tournament)
    db.session.commit()

    return redirect(url_for('tournament.tournaments'))
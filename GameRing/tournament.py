# tournament.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask, jsonify
from flask_login import login_required, current_user
from .models import User, Tournament, Team
from . import db
from datetime import datetime
import json
import os
import stripe

from . import services

tournament = Blueprint('tournament', __name__)
stripe.api_key = "sk_test_51IkuARLHCOtCmyr2UnAXwoyEyXov7TxNUDY64DINcawuBeW7zDxdRIm3oEQa6bAuIi1nRxRbNvJT7lFVLRpFCGJx00OOGFgnwY"


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
        return "This should not happen"

    on_team = False
    in_tournament = False

    current_tournament = False
    payment = False

    if not this_tournament.is_active:
        if datetime.now() > this_tournament.start_at:
            if len(this_tournament.teams) > 2:
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

    if current_user.is_authenticated and current_user.team_id:
        on_team = True
        team = Team.query.get(current_user.team_id)

        if team.tournament_id:
            in_tournament = True

    if on_team:
        if not in_tournament:
            # TODO:  Go to payment here            
            #pre-existing code
            team.tournament_id = tournamentID
            team.participant_id = services.add_participant(tournament.url, team.name)["id"]

        else:
            team.tournament_id = None
            services.remove_participant(tournament.url, team.participant_id)
            team.participant_id = None

        db.session.commit()
    
    #added code
    if not in_tournament:
        return render_template("/tournaments/checkout.html")

    return redirect(url_for('tournament.tournaments'))

# Payment API (Stripe)
def calculate_order_amount(items):
    #make this grab tournament fee and return it
    return 1500

@tournament.route('/tournaments/<string:tournamentID>/create-payment-intent', methods=['POST'])
def create_payment():
    #print("inside create_payment")
    try:
        data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount = calculate_order_amount(data['items']),
            currency = 'usd'
        )

        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error = str(e)), 403


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
        flash(f'Tournament "{name}" already exists')
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


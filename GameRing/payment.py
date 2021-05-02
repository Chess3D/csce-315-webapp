import json
import os
import stripe

# This is a sample test API key. Sign in to see examples pre-filled with your key.
stripe.api_key = "sk_test_51IkuARLHCOtCmyr2UnAXwoyEyXov7TxNUDY64DINcawuBeW7zDxdRIm3oEQa6bAuIi1nRxRbNvJT7lFVLRpFCGJx00OOGFgnwY"

from flask import render_template, jsonify, request, Blueprint, redirect, url_for
from . import db
from .models import Tournament, Team
from .services import add_participant

payment = Blueprint('pay', __name__)


def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    tournament_id = items['tournament']
    tournament = Tournament.query.get(tournament_id)
    entry_fee = tournament.entry_fee
    return int(entry_fee * 100)


def join_tournament(items):
    tournament_id = items['tournament']
    tournament = Tournament.query.get(tournament_id)

    team_id = items['team']
    team = Team.query.get(team_id)

    team.tournament_id = tournament_id
    team.participant_id = add_participant(tournament.url, team.name)["id"]

    db.session.commit()


@payment.route('/checkout')
def checkout():
    tournament_id = request.args['tournament']
    tournament = Tournament.query.get(tournament_id)
    entry_fee = tournament.entry_fee
    return render_template('pay/checkout.html', tournament=tournament_id, team=request.args['team'], entry_fee=entry_fee)


@payment.route('/create-payment-intent', methods=['POST'])
def checkout_post():
    try:
        info = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(info['items'][0]),
            currency='usd'
        )
        return jsonify({
          'clientSecret': intent['client_secret']
        })
    
    except Exception as e:
        return jsonify(error=str(e)), 403


@payment.route('/payment-success', methods=['POST'])
def success():
    try:
        info = json.loads(request.data)
        join_tournament(info['items'][0])

        return jsonify({
          'cat': 'meow'
        })
    except Exception as e:
        return jsonify(error=str(e)), 403


def back_to_about_page():
    return redirect(url_for('tournament.about'))

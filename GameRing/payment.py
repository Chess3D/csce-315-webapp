import json
import os
import stripe

# This is a sample test API key. Sign in to see examples pre-filled with your key.
stripe.api_key = "sk_test_51IkuARLHCOtCmyr2UnAXwoyEyXov7TxNUDY64DINcawuBeW7zDxdRIm3oEQa6bAuIi1nRxRbNvJT7lFVLRpFCGJx00OOGFgnwY"

from flask import render_template, jsonify, request, Blueprint

payment = Blueprint('pay', __name__)


def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400

@payment.route('/checkout')
def checkout():
    return render_template('pay/checkout.html')


@payment.route('/create-payment-intent', methods=['POST'])
def checkout_post():
    try:
        data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd'
        )

        return jsonify({
          'clientSecret': intent['client_secret']
        })
    
    except Exception as e:
        return jsonify(error=str(e)), 403

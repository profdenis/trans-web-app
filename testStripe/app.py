import json
import os

import stripe

# This is a public sample test API key.
# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.
# stripe.api_key = 'sk_test_Hrs6SAopgFPF0bZXSN3f6ELN'
stripe.api_key = os.environ.get('STRIPE_SK') or 'sk_test_Hrs6SAopgFPF0bZXSN3f6ELN'

from flask import Flask, render_template, jsonify, request


app = Flask(__name__)


def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400


@app.route('/checkout')
def checkout():
    amount = 1400
    return render_template('checkout.html', amount=amount)


@app.route('/create-payment-intent', methods=['POST'])
def create_payment():

    try:
        data = json.loads(request.data)
        print(data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403


if __name__ == '__main__':
    app.run()

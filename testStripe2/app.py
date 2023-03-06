
from flask import Flask, session, redirect, render_template, flash, jsonify, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

from forms import LoginForm, RegisterForm
from flask_sqlalchemy import SQLAlchemy

import os
import bcrypt
import json
import stripe

stripe.api_key = os.environ.get('STRIPE_SK') or 'sk_test_Hrs6SAopgFPF0bZXSN3f6ELN'


app = Flask(__name__)

app.secret_key = 'allo'
login_manager = LoginManager()
login_manager.init_app(app)
# without setting the login_view, attempting to access @login_required endpoints will result in an error
# this way, it will redirect to the login page
login_manager.login_view = 'login'
app.config['USE_SESSION_FOR_NEXT'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///users.sqlite'
db = SQLAlchemy(app)

from models import DBUser, Cart, Product, ProductCart


class SessionUser(UserMixin):
    def __init__(self, username, email, phone, cart_id, password=None):
        self.id = username
        self.email = email
        self.phone = phone
        self.password = password
        self.cart_id = cart_id


# this is used by flask_login to get a user object for the current user
@login_manager.user_loader
def load_user(user_id):
    user = find_user(user_id)
    # user could be None
    if user:
        # if not None, hide the password by setting it to None
        user.password = None
    return user


def find_user(username):
    # res = db.session.execute(db.select(DBUser).filter_by(username=username)).first()
    res = DBUser.query.get(username)
    if res:
        # user = SessionUser(res[0].username, res[0].email, res[0].phone, res[0].password)
        user = SessionUser(res.username, res.email, res.phone, res.cart_id, res.password)
    else:
        user = None
    return user


def calculate_order_amount(cart_id):
    total = 0
    products = db.session.execute(
        db.select(Product.product_id, Product.name, Product.price, ProductCart.quantity)
        .where(ProductCart.cart_id == cart_id)
        .where(ProductCart.product_id == Product.product_id)
    )
    for p in products:
        total += p[2] * p[3]
    return total


@app.route('/')
def index():
    try:
        cart = Cart.query.get(current_user.cart_id)
        products = db.session.execute(
            db.select(Product.product_id, Product.name, Product.price, ProductCart.quantity)
            .where(ProductCart.cart_id == cart.cart_id)
            .where(ProductCart.product_id == Product.product_id)
        )
    except:
        cart = None
        products = None
    return render_template('index2.html',
                           username=session.get('username'),
                           cart=cart,
                           products=products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = find_user(form.username.data)
        # user could be None
        # passwords are kept in hashed form, using the bcrypt algorithm
        if user and bcrypt.checkpw(form.password.data.encode(), user.password.encode()):
            login_user(user)
            flash('Logged in successfully.')

            # check if the next page is set in the session by the @login_required decorator
            # if not set, it will default to '/'
            next_page = session.get('next', '/')
            # reset the next page to default '/'
            session['next'] = '/'
            return redirect(next_page)
        else:
            flash('Incorrect username/password!')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    # flash(str(session))
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # check first if user already exists
        user = find_user(form.username.data)
        if not user:
            cart = Cart()
            db.session.add(cart)
            db.session.commit()
            salt = bcrypt.gensalt()
            password = bcrypt.hashpw(form.password.data.encode(), salt)
            user = DBUser(username=form.username.data, email=form.email.data, phone=form.phone.data,
                          password=password.decode(), cart_id=cart.cart_id)
            db.session.add(user)
            db.session.commit()
            flash('Registered successfully.')
            return redirect('/login')
        else:
            flash('This username already exists, choose another one')
    return render_template('register.html', form=form)


@app.route('/protected')
@login_required
def protected():
    products = Product.query.all()
    return render_template('protected.html', products=products)


@app.route('/non_protected')
def non_protected():
    return render_template('non_protected.html')


# @app.route('/cart/<int:product_id>', methods=['POST'])
# @app.route('/cart/<int:product_id>', methods=['DELETE'])
@app.route('/cart/add/<int:product_id>')
@login_required
def add_to_cart(product_id):
    c = Cart.query.get(current_user.cart_id)
    p = Product.query.get(product_id)
    try:
        pc = ProductCart.query.filter_by(cart_id=c.cart_id).filter_by(product_id=p.product_id).one()
        pc.quantity += 1
    except:
        pc = ProductCart(product_id=p.product_id, cart_id=c.cart_id)
    db.session.add(pc)
    db.session.commit()
    return redirect('/')


@app.route('/checkout')
@login_required
def checkout():
    amount = calculate_order_amount(current_user.cart_id)
    return render_template('checkout.html', amount=amount)


@app.route('/create-payment-intent', methods=['POST'])
@login_required
def create_payment():
    try:
        data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(current_user.cart_id),
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

import csv

from flask import Flask, session, redirect, render_template, flash, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'allo'
login_manager = LoginManager()
login_manager.init_app(app)
# without setting the login_view, attempting to access @login_required endpoints will result in an error
# this way, it will redirect to the login page
login_manager.login_view = 'login'
app.config['USE_SESSION_FOR_NEXT'] = True


class User(UserMixin):
    def __init__(self, username):
        self.id = username


# this is used by flask_login to get a user object for the current user
# since we don't have any user information besides the user name, 
# we just create a basic User object from the class above
# the next version will improve on this
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# not a safe way to store and verify passwords, but it will do for now
def check_password(username, password):
    with open('data/passwords.csv') as f:
        for user in csv.reader(f):
            if username == user[0] and password == user[1]:
                return True
    return False


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('login')


@app.route('/')
def index():
    return render_template('index2.html', username=session.get('username'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if check_password(form.username.data, form.password.data):
            login_user(User(form.username.data))
            flash('Logged in successfully.')
            # flash the session only if you're curious
            # don't do this in a live web site!
            # flash(str(session))
            
            # check if the next page is set in the session by the @login_required decorator
            # if not set, it will default to '/'
            next_page = session.get('next', '/')
            # reset the next page to default '/'
            session['next'] = '/'
            # flash(str(session))
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


@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html')


@app.route('/non_protected')
def non_protected():
    return render_template('non_protected.html')


if __name__ == '__main__':
    app.run()

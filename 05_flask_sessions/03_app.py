import csv

from flask import Flask, session, redirect, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'allo'


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
    return render_template('index1.html', username=session.get('username'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if check_password(form.username.data, form.password.data):
            session['username'] = form.username.data
            return redirect('/')
        else:
            flash('Incorrect username/password!')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run()

from flask import Flask, session, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'allo'


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
        # should check if username/password pair is valid
        # for now, just accept everything
        session['username'] = form.username.data
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run()

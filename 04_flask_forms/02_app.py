import csv

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields import EmailField
from wtforms.validators import Email, InputRequired

app = Flask(__name__)
# setting the app's secret key like this is not secure, but for now it's good enough to make it work
app.secret_key = 'allo'


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    message = TextAreaField('Message', validators=[InputRequired()])


@app.route('/contact_form4', methods=['GET', 'POST'])
def handle_contact_form4():
    form = ContactForm()
    if form.validate_on_submit():
        with open('data/messages.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([form.name.data, form.email.data, form.message.data])
        return redirect(url_for('contact_response', name=form.name.data))
    return render_template('04_contact_form.html', form=form)


@app.route('/contact_response/<name>')
def contact_response(name):
    return render_template('05_contact_response.html', name=name)


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'allo'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///contacts.sqlite'
db = SQLAlchemy(app)

from models import Contact, Call


@app.route('/contact/')
def all_contacts():
    contacts = Contact.query.all()
    return render_template('contacts.html', contacts=contacts)


@app.route('/contact/<int:contact_id>')
def contact_by_id(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return render_template('contact.html', contact=contact)


@app.route('/call/')
def all_calls():
    calls = Call.query.all()
    return render_template('calls.html', calls=calls)


@app.route('/call/<int:call_id>')
def call_by_id(call_id):
    call = Call.query.get_or_404(call_id)
    return render_template('call.html', call=call)


if __name__ == '__main__':
    app.run()

from flask import render_template
from . import main
from ..models import Contact, Call


@main.route('/contact/')
def all_contacts():
    contacts = Contact.query.all()
    return render_template('contacts.html', contacts=contacts)


@main.route('/contact/<int:contact_id>')
def contact_by_id(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return render_template('contact.html', contact=contact)


@main.route('/call/')
def all_calls():
    calls = Call.query.all()
    return render_template('calls.html', calls=calls)


@main.route('/call/<int:call_id>')
def call_by_id(call_id):
    call = Call.query.get_or_404(call_id)
    return render_template('call.html', call=call)

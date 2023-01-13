from app import db
import datetime


class Contact(db.Model):
    __tablename__ = 'contact'
    contact_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text())
    phone = db.Column(db.Text())
    address = db.Column(db.Text())
    calls = db.relationship('Call', backref='contact', lazy=True)

    def __repr__(self):
        return f"<Contact {self.contact_id}: {self.name}>"


class Call(db.Model):
    __tablename__ = 'call'
    call_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    phone = db.Column(db.Text(), nullable=False)
    datetime = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
    contact_id = db.Column(db.Integer(), db.ForeignKey('contact.contact_id'))

    def __repr__(self):
        return f"<Call {self.call_id}: {self.phone} {self.contact_id}>"

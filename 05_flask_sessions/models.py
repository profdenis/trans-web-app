from flask_sqlalchemy import SQLAlchemy
from app import db

# db = SQLAlchemy(app)

class DBUser(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.Text(), primary_key=True)
    email = db.Column(db.Text(), nullable=False)
    phone = db.Column(db.Text())
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return "<User {}: {} {}>".format(self.username, self.email, self.phone)

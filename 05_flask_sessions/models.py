from app import db


class DBUser(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.Text(), primary_key=True)
    email = db.Column(db.Text(), nullable=False)
    phone = db.Column(db.Text())
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return "<DBUser {}: {} {}>".format(self.username, self.email, self.phone)

from app import db
import datetime

contact_call = db.Table('contact_call',
                        db.Column('contact_id', db.Integer(), db.ForeignKey('contact.contact_id'), primary_key=True),
                        db.Column('call_id', db.Integer(), db.ForeignKey('call.call_id'), primary_key=True)
                        )


class Contact(db.Model):
    __tablename__ = 'contact'
    contact_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text())
    phone = db.Column(db.Text())
    address = db.Column(db.Text())
    calls = db.relationship('Call', secondary=contact_call, backref=db.backref('calls', lazy=True), lazy=True,
                            viewonly=True)

    def __repr__(self):
        return f"<Contact {self.contact_id}: {self.name}>"


class Call(db.Model):
    __tablename__ = 'call'
    call_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    phone = db.Column(db.Text(), nullable=False)
    datetime = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
    contacts = db.relationship('Contact', secondary=contact_call, backref=db.backref('contacts', lazy=True), lazy=True)

    def __repr__(self):
        return f"<Call {self.call_id}: {self.phone} >"


# Example from chatGPT
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    courses = db.relationship('Course', secondary='student_courses', backref='students')


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class StudentCourses(db.Model):
    __tablename__ = 'student_courses'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

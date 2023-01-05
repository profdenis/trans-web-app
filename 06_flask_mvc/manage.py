from app import app
from models import db, Contact, Call


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Contact=Contact, Call=Call)

# in a terminal, in the project folder, give the command
# flask shell

# then in this special flask shell, give the commands
# db.create_all()
# db.session.commit()

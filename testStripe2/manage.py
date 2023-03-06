from app import app
from models import db, DBUser, Product, Cart, ProductCart


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, DBUser=DBUser, Product=Product, Cart=Cart, ProductCart=ProductCart)

# in a terminal, in the project folder, give the command
# flask shell

# then in this special flask shell, give the commands
# db.create_all()
# db.session.commit()

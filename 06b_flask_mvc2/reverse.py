from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


# def film_to_string(film):
#     return f"<Film {film.film_id}: {film.title}>"


def contact_to_string(contact):
    return f"<Contact {contact.contact_id}: {contact.name}>"


# Connect to the database
# engine = create_engine(r'postgresql://webapps:webapps@localhost:5432/denis')
engine = create_engine(r'sqlite:///instance/contacts.sqlite')

# Reflect the database and generate mapped classes
# Base = automap_base(metadata=MetaData(schema="pagila"))
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create a session
session = Session(engine)

# Print all the mapped classes
print(Base.classes.keys())

# Film = Base.classes.film
# Film.__repr__ = film_to_string
# for f in session.query(Film).all():
#     print(f)

Contact = Base.classes.contact
Contact.__repr__ = contact_to_string

for c in session.query(Contact).all():
    print(c)

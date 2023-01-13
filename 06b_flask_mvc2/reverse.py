from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base


def film_to_string(film):
    return f"<Film {film.film_id}: {film.title}>"


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
from sqlalchemy.orm import Session

session = Session(engine)

# Print all the mapped classes
print(Base.classes.keys())

# Film = Base.classes.film
# for f in session.query(Film).all():
#     print(film_to_string(f))

Contact = Base.classes.contact
for c in session.query(Contact).all():
    print(contact_to_string(c))

#!/usr/bin/python3

"""
script that deletes all State objects with a name containing
the letter a from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id.asc()).all()

    states_to_delete = []
    for state in states:
        if 'a' in state.name:
            states_to_delete.append(state)

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()

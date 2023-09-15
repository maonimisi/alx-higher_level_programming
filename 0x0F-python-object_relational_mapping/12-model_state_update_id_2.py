#!/usr/bin/python3

"""
Script that updates the name of the State object with ID 2 to "New Mexico"
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

    newState = session.query(State).filter_by(id=2).first()

    if newState:
        # Update the state's name
        newState.name = "New Mexico"
        session.commit()
        session.close()
    else:
        print("State with ID 2 not found.")

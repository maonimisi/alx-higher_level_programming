#!/usr/bin/python3

"""
script that prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).first()

    if states is not None:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")

    session.close()

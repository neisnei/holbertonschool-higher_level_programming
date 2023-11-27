#!/usr/bin/python3
"""
Module state objects from db
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    databases = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, databases))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))

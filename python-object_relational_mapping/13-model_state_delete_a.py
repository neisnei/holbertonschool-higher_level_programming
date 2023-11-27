#!/usr/bin/python3
"""
Module deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    my_session = Session()

    for state in session.query(State):
        if "a" in state.name:
        my_session.delete(state)
    my_session.commit()
    my_session.close()

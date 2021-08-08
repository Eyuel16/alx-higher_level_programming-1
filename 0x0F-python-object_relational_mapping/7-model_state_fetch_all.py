#!/usr/bin/python3
"""
return all state objects from database via python
parameters given to script: username, password, database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    for row in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(row.id, row.name))
    session.close()

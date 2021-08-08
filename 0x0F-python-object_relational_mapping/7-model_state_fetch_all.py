#!/usr/bin/python3
"""
contains the class definition of State and instatance Base
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(user, password, database),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session_ = session()
    for row in session_.query(State).order_by(State.id):
        print("{:d}: {:s}".format(row.id, row.name))
    session.close()

#!/usr/bin/python3
"""
contains the class definition of State and instatance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
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
    session_ = sesssion()
    for row in session.query(State).order_by(State.id):
        print("{}: {}".format(row.id, row.name))
    session.close()

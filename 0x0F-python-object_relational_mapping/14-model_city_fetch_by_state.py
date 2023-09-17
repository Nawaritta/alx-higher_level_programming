#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    cities = session.query(City)

    for state in states:
        for city in cities:
            if(state.id == city.state_id):
                print("{}: ({}) {}".format(state.name, city.id, city.name))

#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).outerjoin(City)
    states = query.order_by(State.id, City.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

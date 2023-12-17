#!/usr/bin/python3
""" class state select some object state data"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # list of instances of class state
    filter_objs = session.query(State).filter(State.name.like('%a%'))\
                                      .order_by(State.id).all()
    for st_obj in filter_objs:
        print("{}: {}".format(st_obj.id, st_obj.name))
    session.close()

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
    st_obj = session.query(State).filter(State.name == argv[4]).first()
    if st_obj:
        print(st_obj.id)
    else:
        print("Not found")
    session.close()

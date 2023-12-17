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
    # create new object
    new_st = State(name="Louisiana")
    session.add(new_st)
    session.commit()
    print(new_st.id)
    session.close()

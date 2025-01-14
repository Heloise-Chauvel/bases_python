from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:root@34.46.176.252/sqlalchemy-heloise-exelcia"

#sqlalchemy-heloise-exelcia
#exelcia-heloise:us-central1:exelcia-api
#34.46.176.252

engine = create_engine(DATABASE_URL) #pool de connexions
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
base = declarative_base()

def get_db():
    '''
    associer db à session utilisateur navigateur
    db : singleton d'une session utilisateur
    yield équivalent d'un return
    '''
    db= session_local()
    try:
        yield db
    finally:
        db.close()
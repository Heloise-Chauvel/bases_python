from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from secret_manager import get_secret

value_password = get_secret("db_password_key", "1")

DATABASE_URL = f"mysql+mysqlconnector://root:{value_password}@34.46.176.252/sqlalchemy-heloise-exelcia"

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
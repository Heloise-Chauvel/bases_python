from fastapi import FastAPI
from routers import cars
from database import base, engine

app = FastAPI()

#va chrchr toutes les méthodes qui héritent de base et de les créer sur le pool de connexion engine
base.metadata.create_all(bind=engine)

app.include_router(cars.router, prefix='/cars')

@app.get("/")
def read_root():
    return {"message":"Coucou !"}
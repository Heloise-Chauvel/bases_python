from contextlib import asynccontextmanager

from fastapi import FastAPI
from routers import cars, rentals
from database import base, engine
from pubsub import subscribe_to_message

@asynccontextmanager
async def lifespan(app: FastAPI):
    subscribe_to_message(callback_pubsub)
    yield
    pass

def callback_pubsub(message):
    print(message)

app = FastAPI(lifespan=lifespan, title="Mon appli", version="1.0.0")

#va chrchr toutes les méthodes qui héritent de base et de les créer sur le pool de connexion engine
base.metadata.create_all(bind=engine)

app.include_router(cars.router, prefix='/cars')
app.include_router(rentals.router, prefix='/rentals')

@app.get("/")
def read_root():
    return {"message":"Coucou !"}
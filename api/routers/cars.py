from fastapi import APIRouter, Depends
from schemas import Car, CarCreate
from typing import List
from database import get_db
from sqlalchemy.orm import Session
from models import Car as CarModel

router = APIRouter()

@router.get("/", response_model=List[Car])
async def get_cars(db: Session = Depends(get_db)): #récupère le yield de get_db
    db_cars = db.query(CarModel)
    return []

@router.get("/{car_id}", response_model=Car)
async def get_car_by_id(car_id:int):
    return {}

@router.post("/", response_model=Car)
def create_car(car:CarCreate, db: Session = Depends(get_db)):
    db_car = CarModel(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh()
    #resp = Car(**car.model_dump(), id=1)
    return db_car
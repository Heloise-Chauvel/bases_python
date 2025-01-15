from fastapi import APIRouter, Depends, HTTPException

from auth import get_current_user, get_current_user_admin
from pubsub import publish_message
from schemas import Car, CarCreate
from typing import List
from database import get_db
from sqlalchemy.orm import Session
from models import Car as CarModel
from auth import get_current_user, get_current_user_admin

user_test = None
router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get("/", response_model=List[Car])
async def get_cars(db: Session = Depends(get_db), user: dict = Depends(get_current_user_admin)): #récupère le yield de get_db
    print(user)
    publish_message("Liste des cars")
    db_cars = db.query(CarModel)
    return db_cars

@router.get("/{car_id}", response_model=Car)
async def get_car_by_id(car_id:int, db: Session = Depends(get_db)):
    #db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    db_car = db.query(CarModel).filter(CarModel.id == car_id).one_or_none()
    #if(db_car is None):

    return db_car

@router.post("/", response_model=Car)
def create_car(car:CarCreate, db: Session = Depends(get_db)):
    db_car = CarModel(**car.model_dump())
    db.add(db_car)
    db.commit()
    #db.refresh()
    #resp = Car(**car.model_dump(), id=1)
    return db_car

@router.put("/{car_id}", response_model=Car)
def update_car(car: Car, car_id:int, db: Session = Depends(get_db)):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).one_or_none()
    update_data = car.model.dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_car, key, value)
    db.commit()
    return db_car

@router.delete("/{car_id}", response_model=Car)
def delete_car(car: Car, car_id:int, db: Session = Depends(get_db)):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).one_or_none()
    if(db_car is None):
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(db_car)
    db.commit()
    return db_car
from fastapi import APIRouter, Depends, HTTPException
from schemas import RentalParentSchema, RentalDisplaySchema, RentalCreateSchema
from typing import List
from database import get_db
from sqlalchemy.orm import Session
from models import Car as CarModel

router = APIRouter()

@router.get("/", response_model=List[RentalDisplaySchema])
async def get_rentals(db: Session = Depends(get_db)): #récupère le yield de get_db
    db_rentals = db.query(RentalParentSchema)
    return db_rentals

@router.get("/{rental_id}", response_model=RentalDisplaySchema)
async def get_rental_by_id(rental_id:int, db: Session = Depends(get_db)):
    db_rental = db.query(CarModel).filter(RentalParentSchema.id == rental_id).one_or_none()
    #if(db_car is None):

    return db_rental

@router.post("/", response_model=RentalDisplaySchema)
def create_rental(car:RentalCreateSchema, db: Session = Depends(get_db)):
    db_rental = RentalParentSchema(**car.model_dump())
    db.add(db_rental)
    db.commit()
    #db.refresh()
    #resp = Car(**car.model_dump(), id=1)
    return db_rental
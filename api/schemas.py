# DTO
from pydantic import BaseModel, EmailStr, field_validator, Field
from typing import Optional
import re
from datetime import datetime

class CarModel(BaseModel):
    brand: str
    model: str #= Field(..., description="Model de la voiture")
    #email: EmailStr
    daily_rate: Optional[float] = None
    create_dt: Optional[datetime] = None

    @field_validator("model")
    def validate_model(cls, value):
        if len(value) < 3:
            raise ValueError("Le modèle doit contenir 3 caractères minimum")
        pattern = r"^[A-Za-z]*$"
        if not re.match(pattern, value):
            raise ValueError("Le modèle doit contenir une chaîne de caractères")
        return value

class Car(CarModel):
    id:int
    #fullname: str

class CarCreate(CarModel):
    pass

class RentalParentSchema(BaseModel):
    start_date: datetime
    end_date: datetime
    total_cost: float
    car_id: int

class RentalDisplaySchema(RentalParentSchema):
    id: int
    car: Car
    '''
    A mettre partout sur les display d'objets liés à des tables
    '''
    class Config:
        orm_mode = True

class RentalCreateSchema(RentalParentSchema):
    pass
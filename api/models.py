from database import base
from sqlalchemy import Column, Integer, String, Float

#classe représentative de la table cars
#name="" : nom différent en base
class Car(base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(150), nullable=False, name="brand")
    model = Column(String(150), nullable=False)
    daily_rate = Column(Float, nullable=True)
    create_dt = Column(Float, nullable=False)
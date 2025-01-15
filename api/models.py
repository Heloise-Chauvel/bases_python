from database import base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

#classe représentative de la table cars
#name="" : nom différent en base
class Car(base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(150), nullable=False, name="brand")
    model = Column(String(150), nullable=False)
    daily_rate = Column(Float, nullable=True)
    create_dt = Column(DateTime, nullable=True)

    '''@property
    def full_name(self):
        return f"{self.brand} {self.model}"'''

    #categories = relationship("CategoryModel", secondary="cars_categories", back_populates="cars", lazy="select")


class RentalModel(base):
    __tablename__ = "rental"
    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    total_cost = Column(Float, nullable=False)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=False)

    '''
    lazy select : cherche que quand c'est nécessaire. 
    lazy joined : 1 requête pas 2. 
    lazy subquery : 1 requête séparée
    '''
    car = relationship("Car", lazy='select')
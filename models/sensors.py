""" holds class Sensors"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Date, Float, Boolean, Integer
from sqlalchemy.orm import relationship
from datetime import datetime


class Sensors(BaseModel, Base):
    """Representation of Sensors"""
    __tablename__ = 'sensor'
    soil_humidity_1 = Column(Integer)
    soil_humidity_2 = Column(Integer)
    soil_humidity_3 = Column(Integer)
    air_temperature = Column(Float)
    air_humidity = Column(Float)
    luminosity = Column(Float)

    def __init__(self, *args, **kwargs):
        """initializes Sensors"""
        super().__init__(*args, **kwargs)

    # try change to _dict
    # def to_dict(self):
    #     new_dict = super().to_dict()  # Call the base class's to_dict() method

    #     if self.garden_area:
    #         new_dict["garden_area_name"] = self.garden_area.name

    #     return new_dict

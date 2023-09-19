""" holds class SoilMoistureSet"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer
from datetime import datetime
from sqlalchemy.orm import relationship


class SoilMoistureSet(BaseModel, Base):
    """Representation of SoilMoistureSet"""
    __tablename__ = 'soil_moisture_set'
    humidity_selection = Column(Integer)
    temperature_selection = Column(Integer)
    

    def __init__(self, *args, **kwargs):
        """initializes SoilMoistureSet"""
        super().__init__(*args, **kwargs)

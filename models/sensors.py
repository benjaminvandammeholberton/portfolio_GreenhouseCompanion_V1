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
    air_temperature = Column(Float)
    air_humidity = Column(Float)
    luminosity = Column(Float)

    def __init__(self, *args, **kwargs):
        """initializes Sensors"""
        super().__init__(*args, **kwargs)

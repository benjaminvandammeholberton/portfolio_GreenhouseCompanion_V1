#!/usr/bin/python3
""" holds class VegetableManager"""
import models
from models.base_model import BaseModel, Base
from models.garden_area import GardenArea
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Date, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime


class VegetableManager(BaseModel, Base):
    """Representation of VegetableManager"""
    __tablename__ = 'vegetable_manager'
    name = Column(String(128), nullable=False)
    # Use a different name to store the actual value
    _sowed = Column('sowed', Boolean, default=False)
    planted = Column(Boolean, default=False)
    sowing_date = Column(Date)
    planting_date = Column(Date)
    harvest_date = Column(Date)
    remove_date = Column(Date)
    harvest_quantity = Column(Float)
    notes = Column(String(1024))
    # Add a foreign key to link VegetableManager with GardenArea
    garden_area_id = Column(String(60), ForeignKey('garden_area.id'))
    # Establish the relationship with GardenArea
    garden_area = relationship('GardenArea', backref='vegetable_managers')

    def __init__(self, *args, **kwargs):
        """initializes VegetableManager"""
        super().__init__(*args, **kwargs)

    @property
    def sowed(self):
        return self._sowed

    @sowed.setter
    def sowed(self, value):
        if value and not self._sowed:
            self.sowing_date = datetime.now().date()
        self._sowed = value

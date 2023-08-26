#!/usr/bin/python3
""" holds class VegetableManager"""
import models
from models.base_model import BaseModel, Base
from models.garden_area import GardenArea
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Date, Float, Boolean, Integer
from sqlalchemy.orm import relationship
from datetime import datetime


class VegetableManager(BaseModel, Base):
    """Representation of VegetableManager"""
    __tablename__ = 'vegetable_manager'
    name = Column(String(128), nullable=False)
    quantity = Column(Integer, nullable=False)
    sowed = Column(Boolean, default=False)
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

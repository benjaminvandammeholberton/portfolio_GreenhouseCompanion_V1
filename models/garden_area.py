""" holds class GardenArea"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Float


class GardenArea(BaseModel, Base):
    """Representation of GardenArea """
    __tablename__ = 'garden_area'
    name = Column(String(128), nullable=False, unique=True)
    surface = Column(Float)

    def __init__(self, *args, **kwargs):
        """initializes GardenArea"""
        super().__init__(*args, **kwargs)

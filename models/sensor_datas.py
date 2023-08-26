#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Float


class SensorDatas(BaseModel, Base):
    """Representation of SensorDatas """
    __tablename__ = 'sensor_datas'
    air_temperature = Column(Float, nullable=False)
    soil_temperature = Column(Float, nullable=False)
    air_humidity = Column(Float, nullable=False)
    soil_moisture = Column(Float, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)

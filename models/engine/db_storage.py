"""
Contains the class DBStorage

interacts with a MySQL database

Example Usage:
    storage = DBStorage()
    storage.reload()
    objects = storage.all()
    for obj in objects.values():
        print(obj)

Inputs:
    None

Outputs:
    Methods for interacting with a MySQL database, including querying, adding, deleting, and saving objects.
"""

import models
from models.base_model import BaseModel, Base
from models.vegetable_manager import VegetableManager
from models.garden_area import GardenArea
from models.sensors import Sensors
from models.soil_moisture_set import SoilMoistureSet
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import json

classes = {
    "GardenArea": GardenArea,
    "VegetableManager": VegetableManager,
    "Sensors": Sensors,
    "SoilMoistureSet": SoilMoistureSet
}


class DBStorage:
    """
    interacts with the MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiate a DBStorage object
        """

        
        # Access database configuration values
        # GREENHOUSE_MYSQL_USER = "u105014328_greenhouse_dev"
        # GREENHOUSE_MYSQL_PWD = "Greenhouse_pwd1"
        # GREENHOUSE_MYSQL_HOST = "153.92.220.101"
        # GREENHOUSE_MYSQL_DB = "u105014328_greenhouse"
        # GREENHOUSE_ENV = getenv('HBNB_ENV')

        GREENHOUSE_MYSQL_USER = "greenhouse_dev"
        GREENHOUSE_MYSQL_PWD = "AVNS_I6mOdk372jRm8stpS0d"
        GREENHOUSE_MYSQL_HOST = "db-mysql-ams3-26566-do-user-14634177-0.b.db.ondigitalocean.com"
        GREENHOUSE_MYSQL_DB = "greenhouse_db"
        GREENHOUSE_MYSQL_PORT = 25060
        GREENHOUSE_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.
                                      format(GREENHOUSE_MYSQL_USER,
                                             GREENHOUSE_MYSQL_PWD,
                                             GREENHOUSE_MYSQL_HOST,
                                             GREENHOUSE_MYSQL_PORT,
                                             GREENHOUSE_MYSQL_DB))
        if GREENHOUSE_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session

        Args:
            cls (class): class to query for objects, default is None

        Returns:
            dict: dictionary of objects
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
        add the object to the current database session

        Args:
            obj (object): object to add
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None

        Args:
            obj (object): object to delete
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        reloads data from the database
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        call remove() method on the private session attribute
        """
        self.__session.remove()

    def get(self, cls, id):
        """
        Retrieve an object by class and ID

        Args:
            cls (class): class of the object
            id (str): ID of the object

        Returns:
            object: retrieved object or None if not found
        """
        if cls in classes.values() and type(id) is str:
            key = cls.__name__ + '.' + id
            return self.__session.query(classes[cls.__name__]).get(id)
        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage

        Args:
            cls (class): class to count objects for, default is None

        Returns:
            int: number of objects
        """
        if cls is None:
            total_count = 0
            for clss in classes.values():
                total_count += self.__session.query(clss).count()
            return total_count
        elif cls in classes.values():
            return self.__session.query(cls).count()
        return 0

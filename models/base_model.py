#!/usr/bin/python3
""" BaseModel for AirBnB project. """

import uuid
from datetime import datetime


class BaseModel:
    """main class for AirBnB clone"""

    def __init__(self):
        """
        __init__ : initializes a new instance of basemodel class
        attributes:
            id (str): a unique UUID string for each inst
            create_at: current datetime when an inst is created
            updated_at: current datetime when an inst is updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        __str__ method
        Return:
            a string representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        save method: updates the public instance attribute updated_at
                    with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict method
        Return: dictionary containing all keys/values
                of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        return dict_copy

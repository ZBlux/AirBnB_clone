#!/usr/bin/python3
""" BaseModel for AirBnB project. """

import uuid
from datetime import datetime
import models


class BaseModel:
    """main class for AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """
        __init__ : initializes a new instance of basemodel class
        Parameters:
            *args: arg list. not used
            **kwargs: used to set attributes on the instance.
        attributes:
            id (str): a unique UUID string for each inst set if kwargs empty
            create_at: current datetime when an inst is created
            updated_at: current datetime when an inst is updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        __str__ method
        Return:
            a string representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """
        save method: updates the public instance attribute updated_at
                    with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict method
        Return: a copy of dictionary containing all keys/values
                of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

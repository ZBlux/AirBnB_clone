#!/usr/bin/python3
""" Defines the FileStorage class """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances.
    Attributes:
        __file_path (str): name of the file to save objects to
        __objects (dict): dictionary of instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with the key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to a JSON file.
        """
        with open(self.__file_path, 'w') as f:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects if the file exists.
        """
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                for key, val in objects.items():
                    class_name = val.pop("__class__", None)
                    if class_name in classes:
                        cls = classes[class_name]
                        self.__objects[key] = cls(**val)
                    else:
                        print(f"Unknown class '{class_name}'")
        except FileNotFoundError:
            pass

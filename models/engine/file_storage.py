#!/usr/bin/python3
"""
Defines the FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Class that serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
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
        Deserialize the JSON file to __objects if it exists.
        """
        class_map = {
            "BaseModel": BaseModel,
            "User": User
        }

        try:
            with open(self.__file_path, 'r') as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o.pop("__class__")
                    cls = class_map.get(cls_name)
                    if cls:
                        self.new(cls(**o))
        except FileNotFoundError:
            pass

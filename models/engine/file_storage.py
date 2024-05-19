#!/usr/bin/python3
"""
Defines the FileStorage class
"""
import json


class FileStorage:
    """
    Class that seializes instances to aj Json file and
    deserializes Json file to instances.
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
        Serialize __objects to a Json file.
        """
        with open(self.__file_path, 'w') as f:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        Deserialize the Json file to __objects
        if the file exists
        """
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                for obj in objects.values():
                    cls_name = obj["__class__"]
                    if cls_name == "BaseModel":
                        from models.base_model import BaseModel
                        self.new(BaseModel(**obj))
        except FileNotFoundError:
            pass

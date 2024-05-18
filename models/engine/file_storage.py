#!/usr/bin/python3
"""
Defines the FileStorage class
"""
import json
from models.base_model import BaseModel


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
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with the key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to a Json file.
        """
        with open(FileStorage.__file_path, 'w') as file:
            to_dump = {}
            for k, v in FileStorage.__objects.items():
                to_dump[k] = v.to_dict()
            json.dump(to_dump, file)

    def reload(self):
        """
        Deserialize the Json file to __objects
        if the file exists
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                for obj in json.load(file).values():
                    self.new(BaseModel(**obj))
        except FileNotFoundError:
            pass

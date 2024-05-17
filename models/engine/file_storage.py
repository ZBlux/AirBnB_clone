#!/usr/bin/python3
"""
"""
import json


class FileStorage:
    """
    """
    __filePath = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        """
        key = "{}.{}".formate(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        """

    def reload(self):
        """
        """

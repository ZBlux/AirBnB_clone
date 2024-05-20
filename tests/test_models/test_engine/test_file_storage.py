#!/usr/bin/python3
"""Defines unittests for FileStorage class."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.save()

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all method of FileStorage class."""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn("BaseModel.{}".format(self.obj.id), all_objs)

    def test_new(self):
        """Test new method of FileStorage class."""
        obj_id = self.obj.id
        new_obj = BaseModel()
        self.storage.new(new_obj)
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj_id), all_objs)

    def test_save(self):
        """Test save method of FileStorage class."""
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test reload method of FileStorage class."""
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn("BaseModel.{}".format(self.obj.id), all_objs)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Defines unittests for FileStorage class."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test environment before any test runs."""
        cls.file_path = "test_file.json"
        cls.storage = FileStorage()
        cls.storage._FileStorage__file_path = cls.file_path

    @classmethod
    def tearDownClass(cls):
        """Clean up the test environment after all tests are run."""
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

    def setUp(self):
        """Set up for individual tests."""
        self.obj = BaseModel()
        self.storage.new(self.obj)
        self.storage.save()

    def tearDown(self):
        """Clean up after individual tests."""
        self.storage._FileStorage__objects.clear()

    def test_all(self):
        """Test all method of FileStorage class."""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn("BaseModel.{}".format(self.obj.id), all_objs)

    def test_new(self):
        """Test new method of FileStorage class."""
        new_obj = BaseModel()
        self.storage.new(new_obj)
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_obj.id), all_objs)

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

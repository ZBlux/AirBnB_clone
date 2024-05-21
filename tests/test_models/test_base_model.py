#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
import io
import sys


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_create_instance(self):
        """Test creating an instance of BaseModel."""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, 'id'))
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertTrue(isinstance(instance_dict, dict))
        self.assertTrue('id' in instance_dict)
        self.assertTrue('created_at' in instance_dict)
        self.assertTrue('updated_at' in instance_dict)
        self.assertTrue('__class__' in instance_dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')

    def test_str_representation(self):
        """Test the __str__ method of BaseModel."""
        instance = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            instance.id, instance.__dict__
        )
        self.assertEqual(str(instance), expected_str)

    def test_update_attributes(self):
        """Test updating attributes of BaseModel."""
        instance = BaseModel()
        instance.name = "Test"
        instance.number = 123
        self.assertEqual(instance.name, "Test")
        self.assertEqual(instance.number, 123)

    def test_save_method(self):
        """Test the save method of BaseModel."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        time.sleep(1)
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertGreater(new_updated_at, old_updated_at)

        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print("OK")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "OK")

    def test_create_instance_with_kwargs(self):
        """Test creating an instance with kwargs."""
        now = datetime.now().isoformat()
        instance = BaseModel(id="123", created_at=now, updated_at=now)
        self.assertEqual(instance.id, "123")
        self.assertEqual(instance.created_at.isoformat(), now)
        self.assertEqual(instance.updated_at.isoformat(), now)


if __name__ == '__main__':
    unittest.main()

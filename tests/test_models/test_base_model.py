#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""

import unittest
from models.base_model import BaseModel


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


if __name__ == '__main__':
    unittest.main()

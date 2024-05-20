#!/usr/bin/python3
"""Defines unittests for City class."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_instance(self):
        """Test instantiation of City class."""
        obj = City()
        self.assertIsInstance(obj, City)

    def test_to_dict(self):
        """Test to_dict method of City class."""
        obj = City()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'City')

    def test_str(self):
        """Test __str__ method of City class."""
        obj = City()
        obj_str = str(obj)
        self.assertIsInstance(obj_str, str)


if __name__ == "__main__":
    unittest.main()

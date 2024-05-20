#!/usr/bin/python3
"""Defines unittests for Place class."""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_instance(self):
        """Test instantiation of Place class."""
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_to_dict(self):
        """Test to_dict method of Place class."""
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'Place')

    def test_str(self):
        """Test __str__ method of Place class."""
        obj = Place()
        obj_str = str(obj)
        self.assertIsInstance(obj_str, str)


if __name__ == "__main__":
    unittest.main()

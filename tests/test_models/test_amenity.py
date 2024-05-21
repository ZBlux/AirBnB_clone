#!/usr/bin/python3
"""Defines unittests for Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_attributes(self):
        """Test public class attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_instance(self):
        """Test instantiation of Amenity class."""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_to_dict(self):
        """Test to_dict method of Amenity class."""
        obj = Amenity()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'Amenity')

    def test_str(self):
        """Test __str__ method of Amenity class."""
        obj = Amenity()
        obj_str = str(obj)
        self.assertIsInstance(obj_str, str)


if __name__ == "__main__":
    unittest.main()

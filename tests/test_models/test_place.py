#!/usr/bin/python3
"""Defines unittests for Place class."""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_attributes(self):
        """Test public class attributes."""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, "")
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.amenity_ids, [])

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

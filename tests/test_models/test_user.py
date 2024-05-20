#!/usr/bin/python3
"""Defines unittests for User class."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def test_instance(self):
        """Test instantiation of User class."""
        obj = User()
        self.assertIsInstance(obj, User)

    def test_to_dict(self):
        """Test to_dict method of User class."""
        obj = User()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'User')

    def test_str(self):
        """Test __str__ method of User class."""
        obj = User()
        obj_str = str(obj)
        self.assertIsInstance(obj_str, str)


if __name__ == "__main__":
    unittest.main()

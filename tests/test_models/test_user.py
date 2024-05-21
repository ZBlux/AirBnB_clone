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

    def test_email(self):
        """Test User.email attribute."""
        obj = User()
        self.assertTrue(hasattr(obj, "email"))
        self.assertEqual(obj.email, "")
        obj.email = "user@example.com"
        self.assertEqual(obj.email, "user@example.com")

    def test_password(self):
        """Test User.password attribute."""
        obj = User()
        self.assertTrue(hasattr(obj, "password"))
        self.assertEqual(obj.password, "")
        obj.password = "password123"
        self.assertEqual(obj.password, "password123")

    def test_first_name(self):
        """Test User.first_name attribute."""
        obj = User()
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertEqual(obj.first_name, "")
        obj.first_name = "John"
        self.assertEqual(obj.first_name, "John")

    def test_last_name(self):
        """Test User.last_name attribute."""
        obj = User()
        self.assertTrue(hasattr(obj, "last_name"))
        self.assertEqual(obj.last_name, "")
        obj.last_name = "Doe"
        self.assertEqual(obj.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()

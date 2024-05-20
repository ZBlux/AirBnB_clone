#!/usr/bin/python3
"""Defines unittests for State class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class."""

    def test_instance(self):
        """Test instantiation of State class."""
        obj = State()
        self.assertIsInstance(obj, State)

    def test_to_dict(self):
        """Test to_dict method of State class."""
        obj = State()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'State')

    def test_str(self):
        """Test __str__ method of State class."""
        obj = State()
        obj_str = str(obj)
        self.assertIsInstance(obj_str, str)


if __name__ == "__main__":
    unittest.main()

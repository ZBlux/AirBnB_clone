#!/usr/bin/python3
"""Defines unittests for Review class."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def test_attributes(self):
        """Test public class attributes."""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")

    def test_instance(self):
        """Test instantiation of Review class."""
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_to_dict(self):
        """Test to_dict method of Review class."""
        obj = Review()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'Review')

    def test_str(self):
        """Test __str__ method of Review class."""
        obj = Review()
        obj_str = str(obj)
        self.assertIsInstance(obj_str, str)


if __name__ == "__main__":
    unittest.main()

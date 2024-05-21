#!/usr/bin/python3
"""Defines unittests for console.py."""

import unittest
from unittest.mock import patch
from io import StringIO
import console


class TestConsole(unittest.TestCase):
    """Test cases for the console.py file."""

    def setUp(self):
        """Set up the test environment."""
        self.console = console.HBNBCommand()

    def tearDown(self):
        """Tear down the test environment."""
        pass

    def test_create_command(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(output)

    def test_show_command(self):
        """Test the show command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel")
            output = fake_out.getvalue().strip()
            self.assertIn("** instance id missing **", output)


if __name__ == '__main__':
    unittest.main()

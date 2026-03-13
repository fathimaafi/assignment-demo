"""Unit tests for the greet module."""
import unittest
from greet import greet

class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""
    def test_valid_name(self):
        """Tests greeting with a valid name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_valid_name(self):
        """Tests greeting with a valid name."""
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        
    def test_empty_string(self):
        """Tests greeting with an empty string."""
        self.assertEqual(greet(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test case for the Square class"""

    def test_attributes(self):
        """Test the attributes of the Square class"""
        s = Square(5, 2, 3, 4)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square class"""
        s = Square(5, 2, 3, 4)
        expected_dict = {'id': 4, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

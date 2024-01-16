#!/usr/bin/python3
"""
This module contains the test class TestMaxInteger for the function max_integer.
"""

import unittest
from my_module import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This class contains unittests for the function max_integer.
    """

    def test_max_integer(self):
        """
        This function tests the max_integer function.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertRaises(TypeError, max_integer, [1, "2", 3, 4])
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()

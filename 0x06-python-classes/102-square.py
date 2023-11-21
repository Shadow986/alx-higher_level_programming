#!/usr/bin/python3
"""
This is the "my_module" module.

The my_module module defines the Square class.
"""


class Square:
    """
    This is the Square class.

    The Square class defines a square by its size.
    """

    def __init__(self, size=0):
        """
        This is the constructor method for the Square class.

        The constructor initializes the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        This is a getter method for the Square class.

        The size method retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method for the Square class.

        The size method sets the size of the square.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This is a public instance method for the Square class.

        The area method returns the current square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        This is a special method for the Square class.

        The __eq__ method checks if the square area is equal to the other square area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """
        This is a special method for the Square class.

        The __ne__ method checks if the square area is not equal to the other square area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        """
        This is a special method for the Square class.

        The __lt__ method checks if the square area is less than the other square area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """
        This is a special method for the Square class.

        The __le__ method checks if the square area is less than or equal to the other square area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        This is a special method for the Square class.

        The __gt__ method checks if the square area is greater than the other square area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """
        This is a special method for the Square class.

        The __ge__ method checks if the square area is greater than or equal to the other square area.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()

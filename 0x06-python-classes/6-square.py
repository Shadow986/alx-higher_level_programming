#!/usr/bin/python3
"""
This is the "my_module" module.

The my_module module defines the Square class.
"""


class Square:
    """
    This is the Square class.

    The Square class defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This is the constructor method for the Square class.

        The constructor initializes the size and position of the square.
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        This is a getter method for the Square class.

        The position method retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is a setter method for the Square class.

        The position method sets the position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        This is a public instance method for the Square class.

        The area method returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This is a public instance method for the Square class.

        The my_print method prints the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)))

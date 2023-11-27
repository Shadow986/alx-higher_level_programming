#!/usr/bin/python3
"""This module contains a class Rectangle that defines a rectangle."""


class Rectangle:
    """This class defines a rectangle by its width and height."""

    # Public class attribute to keep track of the number of instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This method initializes a rectangle instance
        with optional width and height parameters."""
        self.width = width
        self.height = height
        # Increment the number of instances during each new instantiation
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This property returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """This setter method sets the width of the
        rectangle to a positive integer value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This property returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """This setter method sets the height of the
        rectangle to a positive integer value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """This method returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """This method returns a string representation of
        the rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """This method returns a string representation of
        the rectangle to be able to recreate a new instance by using eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """This method prints a message when an
        instance of Rectangle is deleted."""
        print("Bye rectangle...")
        # Decrement the number of instances during each instance deletion
        Rectangle.number_of_instances -= 1

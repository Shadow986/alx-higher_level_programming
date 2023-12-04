#!/usr/bin/python3
"""Module for BaseGeometry, Rectangle and Square classes"""


class BaseGeometry:
    """A class for geometric shapes"""

    def area(self):
        """Method that raises an exception for unimplemented area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates an integer value

        Args:
            name (str): the name of the value
            value (int): the value to be validated

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class for rectangles that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method that returns the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """A class for squares that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square instance

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Method that returns the square description"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

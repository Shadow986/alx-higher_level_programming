#!/usr/bin/python3
"""A module that defines a Student class"""


class Student:
    """A class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance

        Args:
            attrs (list of str, optional):
            A list of attribute names to retrieve. Defaults to None.

        Returns:
            dict: A dictionary containing the attributes of the student
        """
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

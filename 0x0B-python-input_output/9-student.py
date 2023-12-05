#!/usr/bin/python3
"""
This module contains a class Student that defines a student by
public instance attributes and a public method
"""


class Student:
    """
    A class Student that defines a student by
    public instance attributes and a public method

    Attributes:
        first_name (str): the first name of the student
        last_name (str): the last name of the student
        age (int): the age of the student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name and age

        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance

        Returns:
            dict: a dictionary containing all
            attributes of the Student instance
        """
        return self.__dict__

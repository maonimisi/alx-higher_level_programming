#!/usr/bin/python3
"""Student to JSON Documentation"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """instantiaton function for the class Student

        Args:
            first_name (str): first name of a student
            last_name (str): last name of a student
            age (int): age of a student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance

        Args:
            attrs (python objects): objects to be returned

        """
        if not isinstance(attrs, list):
            return self.__dict__
        for attributes in attrs:
            if not isinstance(attrs, list):
                return self.__dict__
        new_dict = {}
        for string_attributes in attrs:
            if string_attributes in self.__dict__.keys():
                new_dict[string_attributes] = self.__dict__[string_attributes]
        return new_dict

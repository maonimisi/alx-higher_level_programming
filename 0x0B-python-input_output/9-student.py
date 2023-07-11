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

    def to_json(self):
        """return a dictionary representation of student"""

        return self.__dict__

#!/usr/bin/python3
"""class basegeometry documetnation"""


class BaseGeometry:
    """an empty class BaseGeometry."""

    def area(self):
        """Area function for an instance of a BaseGeometry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate an integer value

        Args:
            name (str): the name(string)
            value (int): the int value to be validated

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Re ctanble that inherit from BaseGeometry"""

    def __init__(self, width, height):
        """instantiation of the rectangle instance

        Args:
            width (int) : the width of the rectangle
            height (int): the height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
"""Rectangle Class Documentation"""


class Rectangle:
    """Initialize an empty class rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation of a rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle instance

        Args:
            value (int): the width of the rectangle instance

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the width of the instance"""

        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle instance

        Args:
            value (int): the height of the rectangle instance

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectagle instance"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a rectagle instance"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

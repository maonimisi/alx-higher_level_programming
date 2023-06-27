#!/usr/bin/python3
"""Documentation for a square class"""


class Square:
    """Represent a square class of a quadilateral with four equal side

    Attributes:
        __size(int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size(int): size of square of a side

        Return:
            None
        Raises:
            ValueError: When the value passed is less than 0
            TypeError: When the value passed is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

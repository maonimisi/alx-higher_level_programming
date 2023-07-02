#!/usr/bin/python3
"""This is a documentaion for add two integer functions"""


def add_integer(a, b=98):
    """Function adds 2 integers

    Args:
        a (int): first value passed
        b (int): second value passed

    Return:
        The sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

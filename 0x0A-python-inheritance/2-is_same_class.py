#!/usr/bin/python3
"""This is an inhrit class checker documentation"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an
        instance of the specified class ; otherwise False.
        Return:
           return True if obj is an instance otherwise, false
    """

    return isinstance(obj, a_class)

#!/usr/bin/python3
"""This is a mylist class documentation"""


class MyList(list):
    """My list class that inherit from list"""

    def print_sorted(self):
        """this function prints list but sorted in
           ascending order"""

        print(sorted(self))

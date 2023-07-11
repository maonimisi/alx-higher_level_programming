#!/usr/bin/python3
"""Append to a file documentation"""


def append_write(filename="", text=""):
    """this function appemmds a string at the end of a text file

    Args:
        text (str): a string of characters to be appended to the file

    Return:
        number of characters added
    """
    with open(filename, 'a', encoding='UTF-8') as myfile:
        return myfile.write(text)

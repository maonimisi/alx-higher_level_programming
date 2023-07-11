#!/usr/bin/python3
"""write file function documentation"""


def write_file(filename="", text=""):
    """ Args:
        text(str) to write to the file
        Return:
        returns the number of text written
    """

    with open(filename, 'w', encoding='UTF-8') as myfile:
        return myfile.write(text)

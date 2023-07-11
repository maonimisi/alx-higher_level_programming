#!/usr/bin/python3
"""Read file function documentation"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, 'r', encoding="UTF-8") as myfile:
        print(myfile.read(), end='')

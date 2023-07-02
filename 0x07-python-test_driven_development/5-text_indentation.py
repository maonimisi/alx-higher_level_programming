#!/usr/bin/python3
"""This is a text indentation documentation"""


def text_indentation(text):
    """Function splits a string of text according to punctuation

    Args:
        text (str): the string of text to split

    Raises:
        TypeError: if the text called with the function is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if char == '.' or char == '?' or char == ':':
                print(char)
                print()
                flag = 0
            else:
                print(char, end='')

#!/usr/bin/python3
"""Creating object from a json file documentation"""


import json


def load_from_json_file(filename):
    """this function creates an object from a 'JSON file'

    Args:
       filename (JSON file): file where an object is created from

    Return:
        JSON object represented by string in the file
    """

    with open(filename, 'r', encoding='UTF-8') as myfile:
        return json.loads(myfile.read())

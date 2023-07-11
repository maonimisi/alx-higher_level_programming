#!/usr/bin/python3
"""Save object to a file documentation"""


import json


def save_to_json_file(my_obj, filename):
    """this function writes an object to a text file, using JSON \
    representation

    Args:
        my_obj (class object): the object to convert to JSON string
        filename (file): the file to write to
    """

    with open(filename, 'w', encoding='UTF-8') as myfile:
        obj_json = json.dumps(my_obj)
        return myfile.write(obj_json)

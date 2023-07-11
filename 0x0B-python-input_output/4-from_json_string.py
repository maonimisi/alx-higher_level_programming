#!/usr/bin/python3
"""From json to object documentation"""


import json


def from_json_string(my_str):
    """this function returns an object(python data structure) represent a
       JSON to string

    Args:
        my_str (JSON string): json string to convert to python object
    Return:
        object - python data structure
    """

    return json.loads(my_str)

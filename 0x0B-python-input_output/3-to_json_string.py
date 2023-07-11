#!/usr/bin/python3
"""Json to string documentation"""

import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string)
        Args:
        my_obj (class object): the object to convert to a JSON string
    Return:
        JSON representation of the object
    """

    return json.dumps(my_obj)

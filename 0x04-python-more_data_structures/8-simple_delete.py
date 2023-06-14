#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return None
    if key in a_dictionary:
        del a_dictionary[key]
    else:
        a_dictionary
    return a_dictionary

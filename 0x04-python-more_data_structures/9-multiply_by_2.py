#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        a_dictionary[key] = value * 2
    return a_dictionary

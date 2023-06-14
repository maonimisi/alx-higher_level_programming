#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None
    new_set = []
    for elem in set_1:
        if elem not in set_2:
            new_set.append(elem)
    for elem in set_2:
        if elem not in set_1:
            new_set.append(elem)
    return new_set

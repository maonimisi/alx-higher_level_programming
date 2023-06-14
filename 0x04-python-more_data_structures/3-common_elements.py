#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set_1 = []
    new_set_2 = []
    if set_1 is None or set_2 is None:
        return None
    for elem in set_1:
        new_set_1.append(elem)
    for elem in set_2:
        new_set_2.append(elem)
    for elem in range(len(new_set_1)):
        if new_set_1[elem] in new_set_2:
            return new_set_1[elem]
        else:
            continue

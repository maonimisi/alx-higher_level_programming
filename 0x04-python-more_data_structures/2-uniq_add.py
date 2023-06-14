#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    new_list = []
    for elem in range(len(my_list)):
        if my_list[elem] not in new_list:
            new_list.append(my_list[elem])
        else:
            continue
    add = 0
    for elem in range(len(new_list)):
        add += new_list[elem]
    return add

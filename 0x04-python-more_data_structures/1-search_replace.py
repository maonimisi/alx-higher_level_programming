#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    new_list = []
    for elem in range(len(my_list)):
        if my_list[elem] != search:
            new_list.append(my_list[elem])
        else:
            new_list.append(replace)
    return new_list

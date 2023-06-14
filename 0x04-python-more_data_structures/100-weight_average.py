#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    score_total = 0
    weight_total = 0
    for score, weight in my_list:
        score_total += score * weight
        weight_total += weight
    if weight_total == 0:
        return 0
    return score_total / weight_total

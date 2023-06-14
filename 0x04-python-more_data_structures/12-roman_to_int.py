#!/usr/bin/python3
import roman


def roman_to_int(roman_string):
    if roman_string is None or roman_string == '':
        return 0
    number = roman.fromRoman(roman_string)
    return number

#!/usr/bin/python3
"""This is a matrix division documentation"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix (list): matrix to be divided
        div (int, fload): number to divide the matrix by

    Return:
       New matrix with each element resultant of the division
    """

    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have \
the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix]
    return new_matrix

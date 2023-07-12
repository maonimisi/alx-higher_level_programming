#!/usr/bin/python3
""""Pascal triangle function documentation"""


def pascal_triangle(n):
    """this functions returns a list of lists of integers representing \
    a pascal triangle

    Args:
        n (int): number of rows of the pascal triangle

    Return:
        pascal triangle - a list of lists
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i-1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)
    return triangle

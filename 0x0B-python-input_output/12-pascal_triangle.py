#!/usr/bin/python3
"""
module with one function pascal_triangle
"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    matrix_pascal = [[1]]

    for _ in range(1, n):
        last_row = matrix_pascal[-1]
        current_row = [1]

        for i in range(1, len(last_row)):
            current_row.append(last_row[i - 1] + last_row[i])

        current_row.append(1)
        matrix_pascal.append(current_row)

    return matrix_pascal

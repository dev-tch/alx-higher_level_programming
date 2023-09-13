#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for list in new_matrix:
        for i  in range(len(list)):
            list[i] = list[i] ** 2
    return (new_matrix)

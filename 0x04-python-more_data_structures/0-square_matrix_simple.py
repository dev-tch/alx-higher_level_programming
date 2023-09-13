#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for list in matrix:
        list_new =[]
        for item in list:
            pow = item ** 2
            list_new.append(pow)
        new_matrix.append(list_new)
    return (new_matrix)

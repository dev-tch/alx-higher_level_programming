#!/usr/bin/python3
"""
this module have one function to divide each list item in matrix
"""


def matrix_divided(matrix, div):
    """ divide each item in matrix by div
    args:
        matrix(list of list): input matrix
        div(int): the value used for division
    Returns:
          List: list contains others list
    """

    # check if matrix of int and float
    # init local variables
    is_item_of_type_list = True
    is_all_values_list_of_type_int = True
    is_matrix_of_type_list = True
    if not isinstance(matrix, list):
        is_matrix_of_type_list = False
    else:
        for item in matrix:
            if not isinstance(item, list):
                is_item_of_type_list = False
                break
            if not all(isinstance(val, (int, float)) for val in item):
                is_all_values_list_of_type_int = False
                break

    if (not is_matrix_of_type_list or matrix == [] or
            not is_item_of_type_list or not is_all_values_list_of_type_int):
        except1 = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(except1)
    # check if all rows of matrix are  same , if not raise except
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    # check if div is int of float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # div can’t be equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # All elements  divided by div, rounded to 2 decimal places
    new_matrix = [[round(val / div, 2) for val in item_m] for item_m in matrix]
    return new_matrix

#!/usr/bin/python3
"""
    Defines a function that divides all elements of a module
    matrix: list of list integers
    div: a number
"""


def matrix_divided(matrix, div):
    """
        divides all elements of a matrix
    """

    new = []
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if (type(div) not in (float, int)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    for r in matrix:
        row = []

        if not isinstance(r, list):
            raise TypeError(err)

        if (len(r) != len(matrix[1])):
            raise TypeError("Each row of the matrix must have the same size")

        for v in r:
            if (type(v) not in (float, int)):
                raise TypeError(err)

            res = round(v / div, 2)
            row.append(res)

        new.append(row)

    return (new)

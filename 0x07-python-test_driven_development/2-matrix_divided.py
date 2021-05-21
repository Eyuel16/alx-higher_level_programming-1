"""
Module 2-matrix_divide
Contains a function to divide all elements if a natrux
recieves a matrix and a divider
"""
def matrix_divided(matrix, div):
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)
    for value in matrix:
        if type(value) is not list:
            raise TypeError(msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    row = len(matrix[0])
    if not all((len(size) == row) for size in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda x: round(x / div, 2), r))for r in matrix])

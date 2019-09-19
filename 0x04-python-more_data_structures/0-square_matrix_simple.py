#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    newm = matrix.copy()
    for i in range(0, len(newm)):
        newm[i] = list(map(lambda x: x*x, newm[i]))
    return newm

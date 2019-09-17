#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    i = len(matrix)
    j = len(matrix[0])
    sp = ""
    for a in range(0, i):
        for b in range(0, j):
            print("{:s}{:d}".format(sp, matrix[a][b]), end="")
            sp = " "
        print("")
        sp = ""

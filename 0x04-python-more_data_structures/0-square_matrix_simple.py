#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        sublist = []
        for number in i:
            sublist.append(number * number)
        new_matrix.append(sublist)
    return new_matrix

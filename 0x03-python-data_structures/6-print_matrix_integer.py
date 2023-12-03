#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        for lists in matrix:
            if len(lists) == 0:
                print()
            else:
                i = 0
                while i < (len(lists) - 1):
                    print("{:d}".format(lists[i]), end=" ")
                    i += 1
                print("{:d}".format(lists[i]))

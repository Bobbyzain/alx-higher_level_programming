#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        j = len(my_list) - 1
        while j >= 0:
            # if type(i) == int:
            if type(my_list[j]) == float:
                print("{:.0f}".format(my_list[j]))
            else:
                print("{:d}".format(my_list[j]))
            j -= 1

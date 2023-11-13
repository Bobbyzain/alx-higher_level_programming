#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if len(my_list) > 0:
        for i in my_list:
            # if type(i) == int:
            if type(i) == float:
                print("{:.0f}".format(i))
            else:
                print("{:d}".format(i))

#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if type(i) != int:
            pass
        else:
            print("{}".format(i))

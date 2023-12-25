#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        i = 0
        j = my_list[0]
        while i < len(my_list):
            if my_list[i] > j:
                j = my_list[i]
            i += 1
    return j

#!/usr/bin/python3
def print_last_digit(number):
    if type(number) != int:
        raise ValueError()
    c = str(number)
    print("{}".format(c[-1]), end='')
    return c[-1]

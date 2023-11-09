#!/usr/bin/python3

def pow(a, b):
    if type(a) != int and type(b) != int:
        raise ValueError()
    return a**b

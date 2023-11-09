#!/usr/bin/python3
def add(a, b):
    if type(a) != int and type(b) != int:
        raise ValueError()
    return a + b

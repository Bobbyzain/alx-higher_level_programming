#!/usr/bin/python3
""" My first class ever!!!.

This module provides the definition of a  square
"""


class Square:
    """ This is an empty class used to deine a square

    This square will be built with subsequent tasks in this project
    """
    def __init__(self, size=0):
        """My init method for defining a square
        Args:
            sides (int): This is the number of sides possessed by the square
        """
        self.__size = size  #: Attribute definition
        """if self.size == 4:
            print("A square {} sides".format(self.size))
        else:
            print("A square actually has 4 sides not {}".format(self.sides))
        """
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

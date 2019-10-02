#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, size=0):
        if size is not None:
            if type(size) != int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

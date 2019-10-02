#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, size=0):
        if size is not None:
            self.__size = size

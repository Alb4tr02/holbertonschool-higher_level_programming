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

    def size(self):
        return self.__size

    def _size(self, value):
        if value is not None:
            if type(value) != int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    size = property(size, _size)

    def my_print(self):
        sep = ""
        for i in range(self.__size):
            sep += "#"
        for i in range(self.__size):
            print("{}".format(sep))
        if self.__size == 0:
            print("")

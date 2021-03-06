#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, size=0, position=(0, 0)):
        if size is not None:
            if type(size) != int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        if position is not None:
            if type(position) != tuple or type(position[0]) != int or\
               type(position[1]) != int or position[0] < 0 or position[1] < 0\
               or len(position) != 2:
                raise\
                    TypeError(
                        "position must be a tuple of 2 positive integers"
                             )
            self.__position = position

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

    def position(self):
        return self.__position

    def _position(self, value):
        if value is not None:
            if type(value) != tuple or type(value[0]) != int or type(value[1])\
               != int or value[0] < 0 or value[1] < 0 or len(value) != 2:
                raise \
                    TypeError(
                        "position must be a tuple of 2 positive integers"
                             )
            self.__position = value

    position = property(position, _position)

    def my_print(self):
        sep = ""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__position[0]):
            sep += " "
        for i in range(self.__size):
            sep += "#"
        for i in range(self.__size):
            print("{}".format(sep))

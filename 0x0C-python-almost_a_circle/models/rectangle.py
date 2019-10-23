#!/usr/bin/python3
"""Module Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.__width = width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """width setter"""
        self.__height = height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.__x = x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.__y = y

#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
        except (TypeError, ValueError) as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        self.__width = width
        self.__height = height

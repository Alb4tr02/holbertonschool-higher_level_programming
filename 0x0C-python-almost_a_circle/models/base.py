#!/usr/bin/python3
class Base:
    """Clase base"""
    __nb_objects = 0

    """Constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

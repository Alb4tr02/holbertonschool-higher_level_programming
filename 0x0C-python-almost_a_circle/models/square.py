#!/usr/bin/python3
""" Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square son of Rectangle :v"""
    def __init__(self, size, x=0, y=0, id=None):
        """Bob :v """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """retrun str"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

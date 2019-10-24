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

    def update(self, *args, **kwargs):
        """update the rectangle"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
        if not (args is not None and len(args) > 0):
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

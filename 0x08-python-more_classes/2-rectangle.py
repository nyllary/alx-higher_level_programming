#!/usr/bin/python3
"""
A rectangle class which checks for the area and
the perimeter of a rectangle
"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """
        init. a new rectangle

        perimeters:
            width: the longest side of the rectangle
            height: how tall the rectangle is
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Represents the width of the rec."""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Reoresents the height of the rec."""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Gets the area of the rec."""

        return self.width * self.height

    def perimeter(self):
        """Gets the total surface area of the rec"""

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

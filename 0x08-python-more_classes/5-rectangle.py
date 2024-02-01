#!/usr/bin/python3
"""
This class defines a rec by its width and height
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """this method sets the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
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
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """
        This method return a string representation of the rectangle
        that can be used to recreate a new instance
        by using eval()
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        This method prints the message 'Bye rectangle...'
        when an instance of Rectangle is deleted.
        """

        print("Bye rectangle...")

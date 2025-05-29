#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def __str__(self):
        return f"{self.brand} shoe, size {self.size}"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) == int or type(value) == float:
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
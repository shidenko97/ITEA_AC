from Serhii_Hidenko.l_8_software_engineering.hw.composite.graphic import (
    Graphic,
)


class Dot(Graphic):
    def __init__(self, x, y):

        self._x = x
        self._y = y

    def draw(self):
        print(self)

    def move(self, x, y):

        self._x += x
        self._y += y

    def __repr__(self):
        return f"Dot ({self._x}, {self._y})"

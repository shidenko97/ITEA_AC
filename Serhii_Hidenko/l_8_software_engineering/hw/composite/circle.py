from Serhii_Hidenko.l_8_software_engineering.hw.composite.dot import Dot


class Circle(Dot):

    def __init__(self, x, y, radius):

        super().__init__(x, y)

        self._radius = radius

    def __repr__(self):
        return f"Circle ({self._x}, {self._y}, {self._radius})"

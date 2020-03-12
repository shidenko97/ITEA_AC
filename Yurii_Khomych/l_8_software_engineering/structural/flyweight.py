import weakref


class Color:
    """Flyweight"""

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ColorFactory:
    """Flyweight Factory"""

    _colors = weakref.WeakValueDictionary()

    @classmethod
    def get_color(cls, name):
        value = cls._colors.get(name)
        if value is None:
            value = Color(name)
            cls._colors[name] = value
        return value


class Placemark:
    """Point on map"""

    def __init__(self, latitude, longitude, color_name):
        # coordinates - internal state (as they are unique for each label)
        self._latitude = latitude
        self._longitude = longitude
        # color - an external state that may be common to different labels
        self._color = ColorFactory.get_color(color_name)

    def __str__(self):
        return (
            f"Color: {self._color}; "
            f"Coordinates: ({self._latitude}, {self._longitude})"
        )


plmrk0 = Placemark(-74.007121, 40.714551, "green")
plmrk1 = Placemark(37.617761, 55.755773, "green")

print(plmrk0)
print(plmrk1)
print(plmrk0._color is plmrk1._color)
plmrk2 = Placemark(37.617761, 55.755773, "red")
print()

class Builder:
    def build_body(self):
        raise NotImplementedError()

    def build_lamp(self):
        raise NotImplementedError()

    def build_battery(self):
        raise NotImplementedError()

    def create_flashlight(self):
        raise NotImplementedError()


class Flashlight:
    """Карманный фонарик"""

    def __init__(self, body, lamp, battery):
        self._shine = False  # излучать свет
        self._body = body
        self._lamp = lamp
        self._battery = battery

    def on(self):
        self._shine = True

    def off(self):
        self._shine = False

    def __str__(self):
        shine = "on" if self._shine else "off"
        return "Flashlight [%s]" % shine


class Lamp:
    """Лампочка"""


class Body:
    """Корпус"""


class Battery:
    """Батарея"""


class FlashlightBuilder(Builder):
    @classmethod
    def build_body(cls):
        return Body()

    @classmethod
    def build_battery(cls):
        return Battery()

    @classmethod
    def build_lamp(cls):
        return Lamp()

    @classmethod
    def create_flashlight(cls):
        lamp = cls.build_lamp()
        body = cls.build_body()
        battery = cls.build_battery()
        return Flashlight(body, lamp, battery)


# builder = FlashlightBuilder()
flashlight = FlashlightBuilder.create_flashlight()
flashlight.on()
print(flashlight)  # Flashlight [on]

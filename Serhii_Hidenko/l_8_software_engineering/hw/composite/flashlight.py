from Serhii_Hidenko.l_8_software_engineering.hw.composite.object_with_status import (
    ObjectWithStatus,
)


class Flashlight(ObjectWithStatus):
    def __init__(self):

        self.__is_on = False

    def show_status(self):
        return "ON" if self.__is_on else "Off"

    def edit_status(self, value):
        self.__is_on = value

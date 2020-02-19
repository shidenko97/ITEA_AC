from Serhii_Hidenko.l_8_software_engineering.hw.composite.object_with_status import ObjectWithStatus


class Notebook(ObjectWithStatus):

    STATUSES = {
        0: "OFF",
        1: "SLEEP",
        2: "ON",
    }

    def __init__(self):

        self.__status = 0

    def show_status(self):
        return self.STATUSES.get(self.__status, "UNDEFINED")

    def edit_status(self, value):

        if value in self.STATUSES.keys():
            self.__status = value
        else:
            raise ValueError("Incorrect status")

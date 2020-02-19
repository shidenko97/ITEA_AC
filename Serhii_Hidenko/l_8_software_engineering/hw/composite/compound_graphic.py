from Serhii_Hidenko.l_8_software_engineering.hw.composite.graphic import Graphic


class CompoundGraphic(Graphic):

    def __init__(self):

        self.__childrens = []

    def add_component(self, component):

        self.__childrens.append(component)

    def remove_component(self, idx):

        return self.__childrens.pop(idx)

    def move(self, x, y):

        for child in self.__childrens:

            child.move(x, y)

    def draw(self):

        for child in self.__childrens:

            child.draw()

from Serhii_Hidenko.l_8_software_engineering.hw.composite.compound_graphic import (
    CompoundGraphic,
)
from Serhii_Hidenko.l_8_software_engineering.hw.composite.dot import Dot
from Serhii_Hidenko.l_8_software_engineering.hw.composite.circle import Circle


class ImageEditor:
    def __init__(self):

        self.__components = CompoundGraphic()

    def load(self):

        self.__components.add_component(Dot(1, 2))
        self.__components.add_component(Circle(1, 2, 3))

    def group_selected(self, components):

        group = CompoundGraphic()
        group.add_component(components)
        self.__components.add_component(group)
        self.__components.draw()

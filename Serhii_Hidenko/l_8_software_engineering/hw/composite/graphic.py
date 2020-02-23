from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass  # Draw graphic

    @abstractmethod
    def move(self, x, y):
        pass  # Move graphic

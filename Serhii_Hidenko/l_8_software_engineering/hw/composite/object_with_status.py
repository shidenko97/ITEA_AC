from abc import ABCMeta, abstractmethod


class ObjectWithStatus(metaclass=ABCMeta):

    @abstractmethod
    def show_status(self):
        pass

    @abstractmethod
    def edit_status(self, value):
        pass

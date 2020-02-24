from abc import ABCMeta, abstractmethod


class AbstractDb(metaclass=ABCMeta):
    @abstractmethod
    def execute_query(self, query, params=None):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

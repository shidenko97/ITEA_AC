class Subject:
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):
        # subscribe to notification
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        # unsubscribe from notification
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.remove(observer)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        # notify all subscribers
        for observer in self._observers:
            observer.update(data)


class ObserverBase:
    """Abstract observer"""

    def update(self, data):
        raise NotImplementedError()


class Observer(ObserverBase):
    def __init__(self, name):
        self._name = name

    def update(self, data):
        print("%s: %s" % (self._name, data))


subject = Subject()
subject.attach(Observer("Observer_1"))
subject.attach(Observer("Observer_2"))
subject.set_data("Data for observers")

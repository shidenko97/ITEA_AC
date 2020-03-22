import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj


class Bird:
    pass


prototype = Prototype()
prototype.register("bird", Bird())

owl = prototype.clone("bird", {"name": "Owl"})
print(type(owl), owl.name)  # Owl

duck = prototype.clone("bird", {"name": "Duck", "color": "black"})
print(type(duck), duck.name)  # Duck

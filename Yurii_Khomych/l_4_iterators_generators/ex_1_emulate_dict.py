# DEFAULT = object()


class TwoWayDict(dict):
    def __init__(self, items=()):
        self.update(items)

    def __delitem__(self, key):
        value = super().pop(key)
        super().pop(value, None)

    def __setitem__(self, key, value):
        if key in self:
            del self[self[key]]
        if value in self:
            del self[value]
        super().__setitem__(key, value)
        super().__setitem__(value, key)

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"

    def update(self, items):
        if isinstance(items, dict):
            items = items.items()
        for key, value in items:
            self[key] = value

    # def pop(self, key, default=DEFAULT):
    #     if key in self or default is DEFAULT:
    #         value = self[key]
    #         del self[key]
    #         return value
    #     else:
    #         return default
    #
    # def setdefault(self, key, value):
    #     if key not in self:
    #         self[key] = value


d = TwoWayDict()
d[3] = 8
# d
# TwoWayDict({3: 8, 8: 3})
d[7] = 6
# d
# TwoWayDict({3: 8, 8: 3, 7: 6, 6: 7})

# but
d.update({9: 7, 8: 2})
# fix with custom update method

# d = TwoWayDict({9: 7, 8: 2})

# add update to init

d = TwoWayDict()
d[9] = 7
# but pop and setdefault doesn't work
d.pop(9)
d.setdefault(4, 2)

# The problem is the pop method doesn’t actually call __delitem__ and
# the setdefault method doesn’t actually call __setitem__

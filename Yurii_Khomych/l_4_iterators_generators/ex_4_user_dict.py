from collections import UserDict


class TwoWayDict(UserDict):
    def __delitem__(self, key):
        value = self[key]
        super().__delitem__(key)
        self.pop(value, None)

    def __setitem__(self, key, value):
        if key in self:
            del self[self[key]]
        if value in self:
            del self[value]
        super().__setitem__(key, value)
        super().__setitem__(value, key)

    def __repr__(self):
        return f"{type(self).__name__}({self.data})"


d = TwoWayDict()
d[3] = 7
del d[7]

d_1 = TwoWayDict()
# d_1
d_1.update({5: 3})
d_1

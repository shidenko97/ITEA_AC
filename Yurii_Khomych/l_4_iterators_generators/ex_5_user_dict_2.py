from collections import UserDict


# without super calls
class TwoWayDict(UserDict):
    def __delitem__(self, key):
        value = self.data.pop(key)
        self.data.pop(value, None)

    def __setitem__(self, key, value):
        if key in self:
            del self[self[key]]
        if value in self:
            del self[value]
        self.data[key] = value
        self.data[value] = key

d = TwoWayDict()
d[3] = 7
del d[7]

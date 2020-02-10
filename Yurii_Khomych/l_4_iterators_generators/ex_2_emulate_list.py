class HoleList(list):

    HOLE = object()

    def __delitem__(self, index):
        self[index] = self.HOLE

    def __iter__(self):
        return (item for item in super().__iter__() if item is not self.HOLE)

    def __eq__(self, other):
        if isinstance(other, HoleList):
            return all(x == y for x, y in zip(self, other))
        return super().__eq__(other)

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"

    # def __ne__(self, other):
    #     return not (self == other)
    #
    # def remove(self, value):
    #     index = self.index(value)
    #     del self[index]
    #
    # def pop(self, index=-1):
    #     value = self[index]
    #     del self[index]
    #     return value


x = HoleList([2, 1, 3, 4])
y = HoleList([1, 2, 3, 5])
del x[0]
del y[1]
del x[-1]
del y[-1]

x == y
list(x), list(y)
x
y

x == y
x != y

# we can define __ne__ but...

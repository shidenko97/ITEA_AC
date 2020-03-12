class InfiniteRepeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

    # Python 2 compatibility:
    def next(self):
        return self.__next__()


rep = InfiniteRepeater(1)
iter_rep = iter(rep)
next(iter_rep)

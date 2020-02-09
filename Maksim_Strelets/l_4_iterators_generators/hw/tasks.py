from collections import UserDict, UserList


# task 3
class UniqDict(dict):
    def __setitem__(self, key, value):
        if self.__len__() > 0:
            return
        super().__setitem__(key, value)

    def __pop__(self):
        return

    def __delitem__(self, key):
        return


class UniqDict2(UserDict):
    def __setitem__(self, key, value):
        if self.__len__() > 0:
            return
        super().__setitem__(key, value)

    def __delitem__(self, item):
        return


# task 4
class IntList(list):
    def append(self, object) -> None:
        if object is not int:
            raise TypeError
        super().append(object)

    def extend(self, iterable) -> None:
        for el in iterable:
            self.append(el)

    def __add__(self, other):
        self.extend(other)

    def __iadd__(self, other):
        self.__add__(other)


class IntList2(UserList):
    def __setitem__(self, key, value):
        if value is not int:
            raise KeyError
        super().__setitem__(key, value)


# task 5
def interleaved(list1, list2):
    res = []
    for i in range(min(len(list1), len(list2))):
        res += [list1[i], list2[i]]
    return res


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

interleaved(a, b)
pass


# task 6
def generator_interleaved(list1, list2):
    for i in range(min(len(list1), len(list2))):
        yield pow(list1[i], list2[i])


q = [el for el in generator_interleaved(a, b)]
pass

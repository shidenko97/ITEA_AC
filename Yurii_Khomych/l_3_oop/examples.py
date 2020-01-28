class Foo:
    pass



obj = Foo()
obj.__class__
# <class '__main__.Foo'>
type(obj)
# <class '__main__.Foo'>
obj.__class__ is type(obj)
# True

for t in int, float, dict, list, tuple:
    print(type(t))

type(type)

type(3)

type(["foo", "bar", "baz"])
# <class 'list'>

t = (1, 2, 3, 4, 5)
type(t)
# <class 'tuple'>


class Foo:
    pass


type(Foo())
my_func = lambda self, a: a

Bar = type("Bar", (Foo,), {"a": 1, "my_func": my_func})

bar = Bar()
result_list = []
for element in range(10):
    Bar = type("Bar", (Foo,), {"element": element, "my_func": my_func})
    bar = Bar()
    bar.my_func()
    result_list.append(bar)

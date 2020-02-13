from enum import Enum

Animal = Enum("Animal", "ant bee cat dog")


class Animal(Enum):
    ant = 1
    bee = 2
    cat = 3
    dog = 4

ANIMAL = {
    "ant": 1,
    "bee": 2,
    "cat": 3,
    "dog": 4,
}
ANIMAL["ant"]
print(Animal.ant)
# <Animal.ant: 1>


class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3


for shake in Shake:
    print(shake)


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


apples = {}
apples[Color.RED] = "red delicious"
apples[Color.GREEN] = "granny smith"
apples == {Color.RED: "red delicious", Color.GREEN: "granny smith"}
# True

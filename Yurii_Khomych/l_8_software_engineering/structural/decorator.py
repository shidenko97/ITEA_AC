class Man:
    def __init__(self, name):
        self._name = name

    def say(self):
        print(f"Hi! My name is {self._name}!")


class Jetpack:
    def __init__(self, man):
        self._man = man

    def __getattr__(self, item):
        return getattr(self._man, item)

    def fly(self):
        # expand the functionality of the object adding the ability to fly
        print(f"{self._man._name} flying on jetpack!")


man = Man("Misha")
# telephone = Telephone(man)
man_jetpack = Jetpack(man)
man_jetpack.say()
man_jetpack.fly()

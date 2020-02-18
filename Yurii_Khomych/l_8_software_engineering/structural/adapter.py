class Dog:
    def __init__(self, name):
        self._name = name

    def bark(self):
        return f"{self._name} bark!"


class Cat:
    def __init__(self, first_name):
        self._name = first_name

    def meow(self):
        return f"{self._name} meow!"


class CatAdapter(Dog):
    # thanks to the adapter we can use
    # interface of the `Dog` class, and the implementation of the` Cat` class.

    def __init__(self, name):
        super().__init__(name=name)
        self._cat = Cat(first_name=name)

    def bark(self):
        # query `bark` converted to request `meow`
        return self._cat.meow()


dog = Dog("Bobik")
print(dog.bark())

dog = CatAdapter("Bobik")

print(dog.bark())

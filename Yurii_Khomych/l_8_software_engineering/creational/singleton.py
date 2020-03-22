class Singleton:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


first_obj = Singleton()
print(id(first_obj))
print(first_obj)

second_obj = Singleton()
print(id(second_obj))
print(second_obj)

print(first_obj is second_obj)

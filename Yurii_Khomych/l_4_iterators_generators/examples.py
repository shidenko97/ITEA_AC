class MyClass_2:
    pass


class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        return "class method called", cls

    @staticmethod
    def staticmethod():
        return "static method called"


obj = MyClass()
obj_2 = MyClass_2()
obj.method()
MyClass.method(obj)
MyClass.method(obj_2)

obj.classmethod()
MyClass.classmethod()

obj.staticmethod()
MyClass.staticmethod()

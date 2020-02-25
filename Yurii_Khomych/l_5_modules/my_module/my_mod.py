s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]


def foo(arg):
    print(f"arg = {arg}")


class Foo:
    pass


def main():
    foo(1)
    foo(2)
    exem = Foo()
    print("Executing as standalone script")
    print(s)
    print(a)
    foo("quux")
    x = Foo()
    print(x)


if __name__ == "__main__":
    main()

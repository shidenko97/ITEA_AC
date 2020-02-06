
a_set = {1, 2, 3}
b_iterator = iter(a_set)
next(b_iterator)
type(a_set)
type(b_iterator)
iter("foobar")  # String

iter(["foo", "bar", "baz"])  # List

iter(("foo", "bar", "baz"))  # Tuple

iter({"foo", "bar", "baz"})  # Set

iter({"foo": 1, "bar": 2, "baz": 3})  # Dict

iter(42)  # Integer

iter(3.1)  # Float

iter(len)  # Built-in function

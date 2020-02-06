from collections import UserList


class OnlyIntList(list):
    """List which apply only integers"""

    def append(self, value) -> None:
        """Append value to the list if it is a int"""

        if not isinstance(value, int):
            raise ValueError("Can apply only integer value")

        super().append(value)

    def extend(self, iterable) -> None:
        """Add each value of iterable through append method"""

        for val in iterable:

            if val.isdigit():
                self.append(int(val))

    def pop(self, index: int = ...) -> str:
        """Just a removing index of list with value returning"""

        val = self[index]
        del self[index]
        return val


class OnlyIntUserList(UserList):
    """
    I don't know how it must works
    """
    pass


if __name__ == "__main__":

    oil = OnlyIntList()
    oil.append(1)  # First setting a value
    print(oil)
    try:
        oil.append({"first_val": 2})  # Second setting a value
    except ValueError as err:
        print(f"{err}")
    print(oil)
    oil.append(-323)  # First setting a value
    print(oil)
    print(oil.pop(0))  # Remove a value
    try:
        oil.extend("1234")  # Third setting a value
    except ValueError as err:
        print(f"{err}")
    print(oil)

    oiul = OnlyIntUserList()
    oiul.append(12)  # First setting a value
    print(oiul)
    try:
        oiul.append({"first_val": 21})  # Second setting a value
    except ValueError as err:
        print(f"{err}")
    print(oiul)
    oiul.append(-3243)  # First setting a value
    print(oiul)
    print(oiul.pop(0))  # Remove a value
    try:
        oiul.extend("12234")  # Third setting a value
    except ValueError as err:
        print(f"{err}")
    print(oiul)

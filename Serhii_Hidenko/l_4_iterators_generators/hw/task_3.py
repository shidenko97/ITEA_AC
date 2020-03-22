from collections import UserDict


class OneUseDict(dict):
    """Dict which can use one key only once"""

    def __init__(self):
        super().__init__()
        self.__used_keys = []

    def update(self, attributes, **kwargs) -> None:
        """Re-declare standard update method for only one write a specific key"""

        for key, value in attributes.items():

            # If key was used - raise AttributeError
            if key in self.__used_keys:
                raise AttributeError(f"You already set key {key} to the dict")

            self[key] = value
            self.__used_keys.append(key)  # Add key to used list

    def pop(self, key) -> str:
        """Just a removing key of dict with value returning"""

        val = self[key]
        del self[key]
        return val


class OneUseUserDict(UserDict):
    """Dict which can use one key only once"""

    def __init__(self):
        super().__init__()
        self.__used_keys = []

    def __setitem__(self, key, value):

        if key in self.__used_keys:
            raise AttributeError(f"You already set key {key} to the dict")

        self.__used_keys.append(key)

        super().__setitem__(key, value)


if __name__ == "__main__":

    oud = OneUseDict()
    oud.update({"first_val": 17})  # First setting a value
    print(oud)
    try:
        oud.update({"first_val": 2})  # Second setting a value
    except AttributeError as err:
        print(f"{err}")
    print(oud)
    oud.update({"second_val": 1})  # First setting a value
    print(oud)
    print(oud.pop("first_val"))  # Remove a value
    try:
        oud.update({"first_val": 3})  # Third setting a value
    except AttributeError as err:
        print(f"{err}")

    ouud = OneUseUserDict()
    ouud.update({"first_val": 14})  # First setting a value
    print(ouud)
    try:
        ouud.update({"first_val": 42})  # Second setting a value
    except AttributeError as err:
        print(f"{err}")
    print(ouud)
    ouud.update({"second_val": 12})  # First setting a value
    print(ouud)
    print(ouud.pop("first_val"))  # Remove a value
    try:
        ouud.update({"first_val": 33})  # Third setting a value
    except AttributeError as err:
        print(f"{err}")

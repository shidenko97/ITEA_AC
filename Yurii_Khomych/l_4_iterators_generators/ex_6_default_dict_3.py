# from collections import defaultdict
#
# defaultdict
slice()


class DefaultDict(dict):
    def __init__(self, *args, default=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def __missing__(self, key):
        return self.default


my_dict = DefaultDict(default=list())

my_dict["Pets"].append(["Bobik", "Barsik"])
my_dict

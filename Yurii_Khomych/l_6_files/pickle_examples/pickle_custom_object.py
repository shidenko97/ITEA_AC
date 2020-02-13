import pickle


class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = (
            {"str": 11, "dex": 12, "con": 10, "int": 16, "wis": 14, "cha": 13}
            if ability_scores is None
            else ability_scores
        )
        self.hp = 10 + self.ability_scores["con"]
        self.my_func = lambda a: a

    def __getstate__(self):
        state = self.__dict__.copy()
        state["my_func"] = None
        return state

    def __setstate__(self, state):
        state["my_func"] = lambda a: a
        self.__dict__.update(state)


elf = Elf(level=4)

with open("my_file.pcl", "wb") as my_file:
    pickle.dump(elf, my_file)

with open("my_file.pcl", "rb") as my_file:
    elf_obj = pickle.load(my_file)
    pass

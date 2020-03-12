import json


class Elf:
    def __init__(self, level, ability_scores=None, hp=None):
        self.level = level
        self.ability_scores = (
            {"str": 11, "dex": 12, "con": 10, "int": 16, "wis": 14, "cha": 13}
            if ability_scores is None
            else ability_scores
        )
        self.ability_scores = ability_scores or {
            "str": 11,
            "dex": 12,
            "con": 10,
            "int": 16,
            "wis": 14,
            "cha": 13,
        }
        self.hp = hp or 10 + self.ability_scores["con"]


class ElfEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Elf):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


elf = Elf(level=4)
# json.dumps(elf)
serialized_elf = json.dumps(elf, cls=ElfEncoder)

deserialized_elf = json.loads(serialized_elf)

elf_instance = Elf(**deserialized_elf)

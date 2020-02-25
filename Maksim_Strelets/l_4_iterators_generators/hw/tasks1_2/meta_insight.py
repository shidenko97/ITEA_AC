class MetaInsight(type):
    def __new__(cls, name, bases, dct):
        temp = super().__new__(cls, name, bases, dct)
        temp.period = {
            "FacebookInsight": 3,
            "GoogleInsight": 7,
            "TwitterInsight": 10,
        }.get(name, 30)
        return temp

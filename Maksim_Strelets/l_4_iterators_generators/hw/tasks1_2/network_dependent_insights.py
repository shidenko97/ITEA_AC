from Maksim_Strelets.l_4_iterators_generators.hw.tasks1_2.base_insight import *


class FacebookInsight(BaseInsight):
    def __init__(self, dimensions_dict=None, dimensions=None, **kwargs):
        self.dimensions_dict = dimensions_dict
        self.dimensions = dimensions
        super().__init__(**kwargs)


class GoogleInsight(BaseInsight):
    def __init__(self, actions=None, **kwargs):
        self.actions = actions
        super().__init__(**kwargs)


class TwitterInsight(BaseInsight):
    def __init__(self, first_date=None, last_date=None, **kwargs):
        self.first_date = first_date
        self.last_date = last_date
        super().__init__(**kwargs)


class SnapchatInsight(BaseInsight):
    def __init__(self, weight=None, type=None, **kwargs):
        self.weight = weight
        self.type = type
        super().__init__(**kwargs)

from Salvador_Sakho.l_2_oop.Home_work.Classes.BaseInsight_class \
    import BaseInsight


class FacebookInsight(BaseInsight):
    def __init__(self, dimensions_dict=None, dimensions=None, **kwargs):
        super().__init__(**kwargs)
        self.dimensions_dict = dimensions_dict
        self.dimensions = dimensions


class GoogleInsight(BaseInsight):
    def __init__(self, actions=None, **kwargs):
        super().__init__(**kwargs)
        self.actions = actions


class TwitterInsight(BaseInsight):
    def __init__(self, first_date=None, last_date=None, **kwargs):
        super().__init__(**kwargs)
        self.first_date = first_date,
        self.last_date = last_date


class SnapchatInsight(BaseInsight):
    def __init__(self, weight=None, type=None, **kwargs):
        super().__init__(**kwargs)
        self.weight = weight,
        self.type = type

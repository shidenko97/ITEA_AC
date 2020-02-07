from BaseInsight import BaseInsight


class GoogleInsight(BaseInsight):

    def __init__(self, actions=None, **kwargs):
        self.actios = actions
        super().__init__(**kwargs)


class FacebookInsight(BaseInsight):

    def __init__(self, dimensions_dict=None, dimensions=None, **kwargs):
        self.dimensions_dict = dimensions_dict
        self.dimensions = dimensions
        super().__init__(**kwargs)


class SnapchatInsight(BaseInsight):

    def __init__(self, weight=None, type=None, **kwargs):
        self.weight = weight
        self.type = type
        super().__init__(**kwargs)


class TwitterInsight(BaseInsight):

    def __init__(self, first_date=None, last_date=None, **kwargs):
        self.first_date = first_date
        self.last_date = last_date
        super().__init__(**kwargs)

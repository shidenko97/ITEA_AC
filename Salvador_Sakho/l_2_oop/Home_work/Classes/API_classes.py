from Salvador_Sakho.l_2_oop.Home_work.Classes.BaseInsight_class \
    import BaseInsight


class FacebookInsight(BaseInsight):
    def __init__(self, *args, **kwargs):
        super(FacebookInsight, self).__init__(*args, **kwargs)
        self.dimensions_dict = kwargs['dimensions_dict']
        self.dimensions = kwargs['dimensions']


class GoogleInsight(BaseInsight):
    def __init__(self, *args, **kwargs):
        super(GoogleInsight, self).__init__(*args, **kwargs)
        self.actions = kwargs['actions']


class TwitterInsight(BaseInsight):
    def __init__(self, *args, **kwargs):
        super(TwitterInsight, self).__init__(*args, **kwargs)
        self.first_date = kwargs['first_date'],
        self.last_date = kwargs['last_date']


class SnapchatInsight(BaseInsight):
    def __init__(self, *args, **kwargs):
        super(SnapchatInsight, self).__init__(*args, **kwargs)
        self.weight = kwargs['weight'],
        self.type = kwargs['type']

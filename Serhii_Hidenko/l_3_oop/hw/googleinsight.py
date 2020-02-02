from Serhii_Hidenko.l_3_oop.hw.baseinsight import BaseInsight


class GoogleInsight(BaseInsight):
    """Google class for insight"""

    def __init__(self, actions=None, **kwargs):

        self.actions = actions

        super().__init__(**kwargs)

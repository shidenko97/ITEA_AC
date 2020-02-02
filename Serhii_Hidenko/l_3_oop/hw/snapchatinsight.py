from Serhii_Hidenko.l_3_oop.hw.baseinsight import BaseInsight


class SnapchatInsight(BaseInsight):
    """Snapchat class for insight"""

    def __init__(self, weight=None, **kwargs):

        self.weight = weight
        self.type = kwargs["type"] if "type" in kwargs else None

        super().__init__(**kwargs)

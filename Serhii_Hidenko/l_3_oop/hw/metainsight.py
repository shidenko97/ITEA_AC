class MetaInsight(type):
    """Metaclass for Insight"""

    def __call__(cls, *args, **kwargs):
        """
        Re-declaring standard __call__ magic method for adding `period` attribute
        :param args: Unnamed arguments
        :type args: tuple
        :param kwargs: Named arguments
        :type kwargs: dict
        :return: Class instance
        :rtype: MetaInsight
        """

        res = super(MetaInsight, cls).__call__(*args, **kwargs)

        api = None

        if "api" in kwargs:
            api = kwargs["api"]

        # get class period by api parameter
        res.period = {
            1: 3,
            2: 7,
            3: 10
        }.get(api, 30)

        # print class name
        print(f"Metaclass instance name {cls.__name__.replace('Insight', '')}")

        return res

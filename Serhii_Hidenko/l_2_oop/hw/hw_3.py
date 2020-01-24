from Yurii_Khomych.l_1_functions.hw_start import insights


class BaseInsight:

    def __init__(self, metric_name=None, api=None, report_name=None, objective=None, unit=None, currency=None,
                 validator_insight_type=None, metric_summary=None, **kwargs):

        self.metric_name = metric_name
        self.api = api
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = kwargs["id"] if "id" in kwargs else None
        self.validator_insight_type = validator_insight_type

        # Check is api a correctly
        self._check_api_is_correct()

        # Create dict of metrics
        self._create_metrics(metric_summary)

    def _check_api_is_correct(self):
        """Check is api attribute a valid value"""

        valid_values = (1, 2, 3, 4)

        if self.api not in valid_values:
            pass  # raise ValueError(f"Incorrect value [{self.api}] for attribute api")

    def _create_metrics(self, metrics):
        """
        Set dict of metrics by insight dict
        :param metrics: List of dict where each element is some metric
        :type metrics: list
        """

        if not isinstance(metrics, dict):
            self.metrics = {}
        else:
            self.metrics = {metric_key: MetricSummary(**metric_params) for metric_key, metric_params in metrics.items()}


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

    def __init__(self, weight=None, **kwargs):

        self.weight = weight
        self.type = kwargs["type"] if "type" in kwargs else None

        super().__init__(**kwargs)


class MetricSummary:

    def __init__(self, metric=None, metric_level=None, metric_average=None, is_outlier=None, true_sign=None, sign=None,
                 mark=None, unit=None, metric_name_frontend=None, mark_key=None, metric_name_frontend_key=None,
                 unit_key=None, **_):

        self.metric = metric
        self.metric_level = metric_level
        self.metric_average = metric_average
        self.is_outlier = is_outlier
        self.true_sign = true_sign
        self.sign = sign
        self.mark = mark
        self.unit = unit
        self.metric_name_frontend = metric_name_frontend
        self.mark_key = mark_key
        self.metric_name_frontend_key = metric_name_frontend_key
        self.unit_key = unit_key


if __name__ == "__main__":

    # Task 1 from README.md
    for insight in insights:

        try:
            bi = FacebookInsight(**insight)
        except ValueError as err:
            print(f"Error: {err}")
        else:
            print(bi.__dict__)

    # Task 2 from README.md
    CLASSES = {
        1: FacebookInsight,
        2: GoogleInsight,
        3: TwitterInsight,
        4: SnapchatInsight
    }

    for insight in insights:

        api_value = insight["api"] if "api" in insight else None

        insight_class = CLASSES.get(api_value, BaseInsight)

        print(f"{insight_class.__name__} class: ", end="\t")

        try:
            bi = insight_class(**insight)
        except ValueError as err:
            print(f"Error: {err}")
        else:
            print(bi.__dict__)

    # Task 3 from README.md
    def insight_builder(insight_dict):
        """"""

        api_val = insight["api"] if "api" in insight_dict else None

        template_class = CLASSES.get(api_val, BaseInsight)

        attributes = [attr for attr in dir(template_class()) if not attr.startswith("__") and
                      not attr.endswith("__") and not attr.startswith("_")]

        return {attribute: insight_dict[attribute] for attribute in attributes if attribute in insight_dict}


    for insight in insights:

        print(insight_builder(insight))

from functools import total_ordering
from Maksim_Strelets.l_2_oop.hw.metric_summary import MetricSummary


@total_ordering
class BaseInsight:
    def __init__(
        self,
        metric_name=None,
        api=None,
        report_name=None,
        objective=None,
        unit=None,
        currency=None,
        id=None,
        validator_insight_type=None,
        **kwargs
    ):
        self.api = api
        self.check_api()

        self.metric_name = metric_name
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metrics = {}

        if "metric_summary" in kwargs.keys():
            self.set_metrics(kwargs["metric_summary"])

    def check_api(self):
        if self.__getattribute__("api") not in range(1, 5):
            raise KeyError("api key must be in (1, 2, 3, 4)")

    def set_metrics(self, metric_summary):
        for key in metric_summary:
            self.metrics[key] = MetricSummary(key, **metric_summary[key])

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __gt__(self, other):
        if self.api != other.api:
            return self.api > other.api
        if self.objective != other.objective:
            return self.objective > other.objective
        return self.id > other.id

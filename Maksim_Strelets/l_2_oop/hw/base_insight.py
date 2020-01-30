from Maksim_Strelets.l_2_oop.hw.metric_summary import MetricSummary


class BaseInsight:
    def __init__(self, metric_name, api, report_name, objective, unit,
                 currency, id, validator_insight_type, **kwargs):
        self.metric_name = metric_name
        self.api = api
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metrics = {}

        if "metric_summary" in kwargs.keys():
            self.set_metrics(kwargs["metric_summary"])

        self.check_api()

    def check_api(self):
        if self.__getattribute__("api") not in range(1, 5):
            raise KeyError("api key must be in (1, 2, 3, 4)")

    def set_metrics(self, metric_summary):
        for key in metric_summary:
            self.metrics[key] = MetricSummary(key, **metric_summary[key])

    def __hash__(self):
        return hash(id)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __gt__(self, other):
        if self.api != other.api:
            return self.api > other.api
        if self.objective != other.objective:
            return self.objective > other.objective
        return self.id > other.id

from hw_start import insights
from Davydenko_Sergii.l_2_oop.MetricSummery import MetricSummary


class BaseInsight:
    def __init__(self, metric_name=None, api=None,
                 report_name=None, objective=None, unit=None,
                 currency=None, id=None, validator_insight_type=None,
                 metric_summary=None, **kwargs):
        self.metric_name = metric_name
        self.api = api
        self.api_met()
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metrics = self.metr_sum(metric_summary)

    # @staticmethod
    def api_met(self):
        if self.api not in range(1, 5):
            raise ValueError(f'Sorry api is not - {self.api}')

    @staticmethod
    def metr_sum(metrics):
        metr_di = {}

        for key, value in metrics.items():
            metr_di[key] = MetricSummary(**value)
        return metr_di

    # @dataclasses
    def __eq__(self, other):
        return hash((self.api, self.objective, self.id)) == hash((other.api, other.objective, other.id))

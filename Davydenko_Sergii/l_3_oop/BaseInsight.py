from hw_start import insights


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
        if self.api == 1:
            self.api == 3
        elif self.api == 2:
            self.api == 7
        elif self.api == 3:
            self.api == 10
        else:
            self.api == 30

from Salvador_Sakho.l_2_oop.Home_work.Classes.MetricSummary_class \
    import MetricSummary


class BaseInsight:
    def __init__(self, metric_name=None,
                 api=None,
                 report_name=None,
                 objective=None,
                 unit=None,
                 currency=None,
                 id=None,
                 validator_insight_type=None,
                 metric_summary=None,
                 **kwargs):
        self.check_api_value(api)
        self.metric_name = metric_name
        self.api = api
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metrics = self.metric_summary_init(metric_summary)

    def check_api_value(self, api_val):
        if api_val not in [1, 2, 3, 4]:
            raise Exception(
                f'Api value is:{api_val}! Expected values: [1, 2, 3, 4]')

    def __eq__(self, comparison_object):
        if isinstance(comparison_object, BaseInsight):
            if self.id != comparison_object.id:
                return False
            elif self.objective != comparison_object.objective:
                return False
            elif self.api != comparison_object.api:
                return False
            else:
                return True

    def metric_summary_init(self, metric_summary):
        for summary_name, values in metric_summary.items():
            return MetricSummary(metric_name=summary_name, **{**values})

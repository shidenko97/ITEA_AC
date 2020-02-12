from Salvador_Sakho.l_2_oop.Home_work.Classes.MetricSummary_class \
    import MetricSummary


class BaseInsight:
    def __init__(self, metric_name, api, report_name, objective, unit, currency
                 , id, validator_insight_type, **kwargs):
        self.check_api_value(api)
        self.metric_name = metric_name
        self.api = api
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type

    def check_api_value(self, api_val):
        if api_val not in [1, 2, 3, 4]:
            raise Exception('Not sure, but something goes wrong!')

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

    def metric_summary_init(self, **kwargs):
        return MetricSummary(
            self.metric_name, self.api, self.report_name, self.objective,
            self.unit, self.currency, self.id, self.validator_insight_type
            , **kwargs)

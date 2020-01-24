class BaseInsight:
    def __init__(self, metric_name, api, report_name, objective, unit,
                 currency, id, validator_insight_type, **kwargs):
        locals_dump = locals().copy()
        del locals_dump['self']
        del locals_dump['kwargs']
        for key in locals_dump:
            if key.startswith("__"):
                continue
            setattr(self, key, locals_dump[key])
        self.metrics = {}

        if "metric_summary" in kwargs.keys():
            self.set_metrics(kwargs["metric_summary"])

        self.check_api()

    def check_api(self):
        if self.__getattribute__("api") not in range(1,5):
            raise KeyError("api key must be in (1, 2, 3, 4)")

    def set_metrics(self, metric_summary):
        for key in metric_summary:
            self.metrics[key] = MetricSummary(key, **metric_summary[key])


class MetricSummary:
    def __init__(self, metric_name, metric, metric_level, metric_average,
                 is_outlier, true_sign, sign, mark, unit,
                 metric_name_frontend, mark_key, metric_name_frontend_key,
                 unit_key, **kwargs):
        locals_dump = locals().copy()
        del locals_dump['self']
        del locals_dump['kwargs']
        for key in locals_dump:
            if key.startswith("__"):
                continue
            setattr(self, key, locals_dump[key])

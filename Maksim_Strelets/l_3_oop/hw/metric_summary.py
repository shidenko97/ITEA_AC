class MetricSummary:

    def __init__(self, metric_name, metric, metric_level, metric_average,
                 is_outlier, true_sign, sign, mark, unit,
                 metric_name_frontend, mark_key, metric_name_frontend_key,
                 unit_key, **kwargs):
        locals_dump = locals().deepcopy()
        del locals_dump['self']
        del locals_dump['kwargs']
        for key in locals_dump:
            if key.startswith("__"):
                continue
            setattr(self, key, locals_dump[key])

    def sum(self):
        return sum([
            x
            for x in self.__dict__.items()
            if isinstance(x, int) or isinstance(x, float)
        ])

class MetricSummary:

    def __init__(self, metric, metric_level, metric_average, is_outlier, true_sign,
                 sign, mark, unit, metric_name_frontend, mark_key, metric_name_frontend_key,
                 unit_key):

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


    def __repr__(self):
        return f'{self.__dict__}'
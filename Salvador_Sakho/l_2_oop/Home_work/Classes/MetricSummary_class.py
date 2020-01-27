class MetricSummary():
    def __init__(self, metric, metric_level, metric_average, is_outlier,
                 true_sign, sign, mark, unit, metric_name_frontend, mark_key,
                 metric_name_frontend_key, unit_key):
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

    def get_metric(self):
        return self.metric

    def get_metric_level(self):
        return self.metric_level

    def get_metric_average(self):
        return self.metric_average

    def get_is_outlier(self):
        return self.is_outlier

    def get_true_sign(self):
        return self.true_sign

    def get_sign(self):
        return self.sign

    def get_mark(self):
        return self.mark

    def get_unit(self):
        return self.unit

    def get_metric_name_frontend(self):
        return self.metric_name_frontend

    def get_mark_key(self):
        return self.mark_key

    def get_metric_name_frontend_key(self):
        return self.metric_name_frontend_key

    def get_unit_key(self):
        return self.unit_key

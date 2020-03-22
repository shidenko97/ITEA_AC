class MetricSummary:
    def __init__(self, metric_name=None, **values):
        self.metric_name = metric_name
        self.metric = values['metric']
        self.metric_level = values['metric_level']
        self.metric_average = values['metric_average']
        self.is_outlier = values['is_outlier']
        self.true_sign = values['true_sign']
        self.sign = values['sign']
        self.mark = values['mark']
        self.unit = values['unit']
        self.metric_name_frontend = values['metric_name_frontend']
        self.mark_key = values['mark_key']
        self.metric_name_frontend_key = values['metric_name_frontend_key']
        self.unit_key = values['unit_key']

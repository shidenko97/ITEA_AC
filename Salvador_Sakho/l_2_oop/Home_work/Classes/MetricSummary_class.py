class MetricSummary:
    def __init__(self, *args, **kwargs):
        self.metric = args['metric']
        self.metric_level = args['metric_level']
        self.metric_average = args['metric_average']
        self.is_outlier = args['is_outlier']
        self.true_sign = args['true_sign']
        self.sign = args['sign']
        self.mark = args['mark']
        self.unit = args['unit']
        self.metric_name_frontend = args['metric_name_frontend']
        self.mark_key = args['mark_key']
        self.metric_name_frontend_key = args['metric_name_frontend_key']
        self.unit_key = args['unit_key']

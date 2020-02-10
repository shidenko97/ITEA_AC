from Salvador_Sakho.l_2_oop.Home_work.Classes.BaseInsight_class \
    import BaseInsight


class MetricSummary(BaseInsight):
    def __init__(self, *args, **kwargs):
        super(MetricSummary, self).__init__(*args, **kwargs)
        self.metric = kwargs['metric_summary']['metric']
        self.metric_level = kwargs['metric_summary']['metric_level']
        self.metric_average = kwargs['metric_summary']['metric_average']
        self.is_outlier = kwargs['metric_summary']['is_outlier']
        self.true_sign = kwargs['metric_summary']['true_sign']
        self.sign = kwargs['metric_summary']['sign']
        self.mark = kwargs['metric_summary']['mark']
        self.unit = kwargs['metric_summary']['unit']
        self.metric_name_frontend = kwargs['metric_summary'][
            'metric_name_frontend']
        self.mark_key = kwargs['metric_summary']['mark_key']
        self.metric_name_frontend_key = kwargs['metric_summary'][
            'metric_name_frontend_key']
        self.unit_key = kwargs['metric_summary']['unit_key']

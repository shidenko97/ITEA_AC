import Salvador_Sakho.l_2_oop.Home_work.hw_start as hw_start
from Salvador_Sakho.l_2_oop.Home_work.Classes.MetricSummary_class \
    import MetricSummary


class BaseInsight:
    _task_1_dict = {}
    _metrics = {'cpc': []}

    def __init__(self):
        for list_element in hw_start.insights:
            for key, val in list_element.items():
                if key in ["metric_name", "api", "report_name", "objective",
                           "unit", "currency", "id", "validator_insight_type",
                           'metric_summary', 'dimensions', 'dimensions_dict',
                           'actions', 'first_date', 'last_date', 'weight',
                           'type']:
                    if key in self._task_1_dict.keys():
                        self._task_1_dict[key].append(val)
                    else:
                        self._task_1_dict[key] = [val]

    def check_api_value(self):
        if sum(1 for data in self._task_1_dict['api'] if
               data < 1 or data > 4) > 0:
            raise Exception('Not sure, but something goes wrong!')
        else:
            print('Issues in main "api" data, were not detected')

    def get_task_1_dict(self):
        self.check_api_value()
        return self._task_1_dict

    def insight_builder(self, keys_value):
        return [self.get_task_1_dict().get(data) for data in keys_value]

    def get_metrics(self):
        return self.__metric_summary_init()

    def __metric_summary_init(self):
        some_data = self._task_1_dict['metric_summary']
        for data in some_data:
            self._metrics['cpc'].append(MetricSummary(
                data['cpc']['metric']
                , data['cpc']['metric_level']
                , data['cpc']['metric_average']
                , data['cpc']['is_outlier']
                , data['cpc']['true_sign']
                , data['cpc']['sign']
                , data['cpc']['mark']
                , data['cpc']['unit']
                , data['cpc']['metric_name_frontend']
                , data['cpc']['mark_key']
                , data['cpc']['metric_name_frontend_key']
                , data['cpc']['unit_key']))

        return self._metrics

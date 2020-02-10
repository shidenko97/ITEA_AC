import Salvador_Sakho.l_2_oop.Home_work.hw_start as hw_start


class BaseInsight:
    _task_1_dict = {}
    metrics = {}

    def __pars_data_source(self):
        for list_element in hw_start.insights:
            for key, val in list_element.items():
                if key in self._task_1_dict.keys():
                    self._task_1_dict[key].append(val)
                else:
                    self._task_1_dict[key] = [val]

    def __init__(self, metric_name, api, report_name, objective, unit, currency
                 , id, validator_insight_type, **kwargs):
        self.check_api_value(api)
        self.__pars_data_source()
        self.metric_name = metric_name
        self.api = api
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metrics = {'cpc': self._task_1_dict['metric_name']}

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
        from Salvador_Sakho.l_2_oop.Home_work.Classes.MetricSummary_class \
            import MetricSummary
        return MetricSummary(
            self.metric_name, self.api, self.report_name, self.objective,
            self.unit, self.currency, self.id, self.validator_insight_type
            , **kwargs)

    def insight_builder(self, api_num):
        from Salvador_Sakho.l_2_oop.Home_work.Classes.API_classes import \
            FacebookInsight, GoogleInsight, TwitterInsight, SnapchatInsight

        if api_num == 1:
            dimensions_dict_generator \
                = iter(data for data in self._task_1_dict['dimensions_dict'])
            dimensions_generator = iter(self._task_1_dict['dimensions'])

            return FacebookInsight(
                self.metric_name, self.api, self.report_name,
                self.objective, self.unit, self.currency, self.id,
                self.validator_insight_type
                , dimensions_dict=next(dimensions_dict_generator)
                , dimensions=next(dimensions_generator)
            )
        elif api_num == 2:
            actions_generator = iter(self._task_1_dict['actions'])
            return GoogleInsight(
                self.metric_name, self.api, self.report_name,
                self.objective, self.unit, self.currency, self.id,
                self.validator_insight_type
                , actions=next(actions_generator)
            )
        elif api_num == 3:
            last_date_generator = iter(self._task_1_dict['last_date'])
            first_date_generator = iter(self._task_1_dict['first_date'])
            return TwitterInsight(
                self.metric_name, self.api, self.report_name,
                self.objective, self.unit, self.currency, self.id,
                self.validator_insight_type
                , first_date=next(first_date_generator)
                , last_date=next(last_date_generator)
            )
        elif api_num == 4:
            weight_generator = iter(self._task_1_dict['weight'])
            type_generator = iter(self._task_1_dict['type'])
            return SnapchatInsight(
                self.metric_name, self.api, self.report_name,
                self.objective, self.unit, self.currency, self.id,
                self.validator_insight_type
                , weight=next(weight_generator)
                , type=next(type_generator)
            )

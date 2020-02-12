from Salvador_Sakho.l_2_oop.Home_work import hw_start
from Salvador_Sakho.l_2_oop.Home_work.Classes.API_classes import \
    FacebookInsight, GoogleInsight, TwitterInsight, SnapchatInsight

_task_1_dict = {}
metrics = {}


def __pars_data_source(self):
    for list_element in hw_start.insights:
        for key, val in list_element.items():
            if key in self._task_1_dict.keys():
                self._task_1_dict[key].append(val)
            else:
                self._task_1_dict[key] = [val]


def insight_builder(api_num, *args):
    metric_name = args[0]
    api = args[1]
    report_name = args[2]
    objective = args[3]
    unit = args[4]
    currency = args[5]
    id = args[6]
    validator_insight_type = args[6]
    if api_num == 1:
        dimensions_dict_generator \
            = iter(data for data in _task_1_dict['dimensions_dict'])
        dimensions_generator = iter(_task_1_dict['dimensions'])
        return FacebookInsight(
            metric_name, api, report_name,
            objective, unit, currency, id,
            validator_insight_type
            , dimensions_dict=next(dimensions_dict_generator)
            , dimensions=next(dimensions_generator)
        )
    elif api_num == 2:
        actions_generator = iter(_task_1_dict['actions'])
        return GoogleInsight(
            metric_name, api, report_name,
            objective, unit, currency, id,
            validator_insight_type
            , actions=next(actions_generator)
        )
    elif api_num == 3:
        last_date_generator = iter(_task_1_dict['last_date'])
        first_date_generator = iter(_task_1_dict['first_date'])
        return TwitterInsight(
            metric_name, api, report_name,
            objective, unit, currency, id,
            validator_insight_type
            , first_date=next(first_date_generator)
            , last_date=next(last_date_generator)
        )
    elif api_num == 4:
        weight_generator = iter(_task_1_dict['weight'])
        type_generator = iter(_task_1_dict['type'])
        return SnapchatInsight(
            metric_name, api, report_name,
            objective, unit, currency, id,
            validator_insight_type
            , weight=next(weight_generator)
            , type=next(type_generator)
        )

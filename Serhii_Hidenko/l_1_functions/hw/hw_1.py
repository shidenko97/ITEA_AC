from pprint import pprint
from hw_start import insights


def recursive_remove_unused(dict_block, unused) -> dict:
    """
    Recursive removes from `dict_block` keys from `unused`
    :param dict_block: Dictionary for analyze
    :type dict_block: dict
    :param unused: Dictionary to remove
    :type unused: dict
    :return: Result dictionary
    :rtype: dict
    """

    result_dict = {}

    for item_key, item_value in dict_block.items():

        if item_key not in unused.keys():
            result_dict[item_key] = item_value
        else:
            if unused[item_key] is None:
                pass
            elif isinstance(unused[item_key], dict):

                if isinstance(item_value, dict):
                    result_dict[item_key] = recursive_remove_unused(item_value, unused[item_key])
                elif isinstance(item_value, list):

                    sub_list = []

                    for list_item in item_value:
                        sub_list.append(recursive_remove_unused(list_item, unused[item_key]))

                    result_dict[item_key] = sub_list

    return result_dict


def get_insight_sort_string(insight) -> str:
    """
    Get a string of insight sort parameters
    :param insight: Insight to be analyzed
    :type insight: dict
    :return: String of sort parameters
    :rtype: str
    """

    sort_string = ""
    sort_keys = ("type", "api", "report_name", "objective")

    for key in sort_keys:

        if key in insight:
            sort_string += key

    return sort_string


def transform_param(insight, param, func) -> dict:
    """
    Change `param` of `insight` by `func`
    :param insight: Insight to be analyzed
    :type insight: dict
    :param param: Parameter to changed
    :type param: str
    :param func: Function for parameter changing
    :type func: Any
    :return: Insight with a transformed parameter
    :rtype: dict
    """

    if param in insight.keys():
        insight[param] = func(insight[param])

    return insight


def recursive_find_parameter(insight, parameter) -> list:

    result = []

    for key, value in insight.items():

        if key == parameter:
            result.append(value)
        elif isinstance(value, dict):
            result.extend(recursive_find_parameter(value, parameter))
        elif isinstance(value, list):

            for item in value:

                if isinstance(item, dict):
                    result.extend(recursive_find_parameter(item, parameter))

    return result


UNUSED_KEYS = {
    "period": None,
    "count": None,
    "total_count": None,
    "page_id": None,
    "entities_affected": {
        "entities": {
            "link": None,
            "status": None,
            "days_in_data": None
        }
    }
}

result = []
list_of_objectives = []
insights_campaigns = {}

i = 0

for insight in insights:

    i += 1

    # First task in README.md
    result.append(recursive_remove_unused(insight, UNUSED_KEYS))

    # Second task in README.md
    if "entities_affected" in insight and "table_columns" in insight["entities_affected"]:

        table_columns = []

        for table_column in insight["entities_affected"]["table_columns"]:

            if ("unit" in table_column and table_column["unit"] == "EUR") or "unit" not in table_column:
                table_columns.append(table_column)

        insight["entities_affected"]["table_columns"] = table_columns

    if "metric_sums" in insight:

        metrics_sums = []

        for metric_sum in insight["metric_sums"]:

            if ("unit_key" in metric_sum and metric_sum["unit_key"] == "EUR") or "unit_key" not in metric_sum:
                metrics_sums.append(metric_sum)

        insight["metric_sums"] = metrics_sums

    # Third task in README.md
    if ("objective" in result[-1].keys()) and (objective := result[-1]["objective"]):
        list_of_objectives.append(objective)

    insights_campaigns[i] = recursive_find_parameter(insight, "campaign_id")

    # Seventh task in README.md
    if "metric_sums" in insight.keys():
        sums = list(map(lambda metric_sum: metric_sum["sum"], insight["metric_sums"]))
        sum_levels = list(map(lambda metric_sum: metric_sum["sum_level"], insight["metric_sums"]))
        sum_generals = list(map(lambda metric_sum: metric_sum["sum_general"], insight["metric_sums"]))

        for each_metric in (sums, sum_levels, sum_generals):
            metrics_sum = sum(each_metric)
            # print(f"Sum: {metrics_sum}, Avg: {metrics_sum / len(each_metric)}")

    # Ninth and tenth task in README.md
    # print(transform_param(insight, "report_name", lambda a: a.upper() if a == "device" else a))
    # print(transform_param(insight, "page_id", lambda a: None if a == "(not set)" else a))

# Fourth task in README.md
dict_of_objectives = dict(map(lambda i: (i, list_of_objectives[i]), range(len(list_of_objectives))))

# Sixth task in README.md
unique_objectives = set(list_of_objectives)

# Eighth task in README.md
sorted_insights = sorted(insights, key=lambda i: get_insight_sort_string(i))

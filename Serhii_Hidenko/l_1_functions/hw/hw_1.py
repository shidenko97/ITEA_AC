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

for insight in insights:

    # First task in README.md
    result.append(recursive_remove_unused(insight, UNUSED_KEYS))

    # Third task in README.md
    if ("objective" in result[-1].keys()) and (objective := result[-1]["objective"]):
        list_of_objectives.append(objective)

# Fourth task in README.md
dict_of_objectives = dict(map(lambda i: (i, list_of_objectives[i]), range(len(list_of_objectives))))

print(dict_of_objectives)

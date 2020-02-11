from hw_start import insights
from Remove_unused import SORT_KEY
# mayb Done


def make_value(insights, sort_key):
    result = []

    for keys in sort_key:
        for in_keys in insights:
            if keys in in_keys:
                result.append(in_keys)
        return print(result)


make_value(insights, SORT_KEY)

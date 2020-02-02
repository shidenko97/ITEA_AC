from hw_start import insights
# from operator import itemgetter, attrgetter, methodcaller
from Remove_unused import sort_key
# mayb Done


def eight_cond(insights, sort_key):
    result = []

    for keys in sort_key:
        for in_keys in insights:
            if keys in in_keys:
                result.append(in_keys)
        return print(result)


eight_cond(insights, sort_key)

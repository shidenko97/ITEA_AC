from hw_start import insights
from Remove_unused import METR_LIST, METR_SUMS
# Done


def first_check(insights):
    if isinstance(insights, dict):
        for key, value in insights.items():
            if key == METR_SUMS:
                for i in map(dict, value):
                    return print(f"The sums M_S is {i['sum'] + i['sum_level'] + i['sum_general']}, "
                                 f"and average M_S is ")
            else:
                first_check(value)

    elif isinstance(insights, list):
        for insight in insights:
            first_check(insight)


first_check(insights)

from hw_start import insights
from Remove_unused import *
# Done


def sec_condition(insights):
    if isinstance(insights, dict):

        copy_insights = insights.copy()
        for key, value in insights.items():
            if key in unit_keys:
                if value != 'EUR':
                    del copy_insights[key]

            else:
                sec_condition(value)
        return print(copy_insights)

    elif isinstance(insights, list):
        for insight in insights:
            sec_condition(insight)


print(sec_condition(insights))

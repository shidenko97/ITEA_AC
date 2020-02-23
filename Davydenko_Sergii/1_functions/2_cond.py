from hw_start import insights
from Remove_unused import UNIT_KEYS


# Done


def remove_keys(insights):
    if isinstance(insights, dict):

        copy_insights = insights.copy()
        for key, value in insights.items():
            if key in UNIT_KEYS:
                if value != "EUR":
                    del copy_insights[key]

            else:
                remove_keys(value)
        return print(copy_insights)

    elif isinstance(insights, list):
        for insight in insights:
            remove_keys(insight)


remove_keys(insights)

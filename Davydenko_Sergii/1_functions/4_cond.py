from hw_start import insights
from Remove_unused import obj_dict
# Done, mayb

def four_cond(insights):
    result = []
    mix = {}

    if isinstance(insights, dict):
        for key, value in insights.items():
            if key == obj_dict:
                mix[key] = value
                result.append(mix)
                return print(result)

    elif isinstance(insights, list):
        for insight in insights:
            four_cond(insight)


four_cond(insights)

from hw_start import insights
from Remove_unused import OBJ_DICT
# Done, mayb

def all_ins_o_in_dict(insights):
    result = []
    mix = {}

    if isinstance(insights, dict):
        for key, value in insights.items():
            if key == OBJ_DICT:
                mix[key] = value
                result.append(mix)
                return print(result)

    elif isinstance(insights, list):
        for insight in insights:
            all_ins_o_in_dict(insight)


all_ins_o_in_dict(insights)

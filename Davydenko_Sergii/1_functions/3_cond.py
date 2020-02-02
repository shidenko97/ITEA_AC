from hw_start import insights
from Remove_unused import obj_key
# Done


def get_obj(insights):
    result_bj = []

    if isinstance(insights, dict):

        for key, value in insights.items():
            if key == obj_key:
                result_bj.append(key)
                return print(f"{result_bj}")  # HOW can do _1, _2 ... >??????
            else:
                get_obj(value)

    elif isinstance(insights, list):
        for insight in insights:
            get_obj(insight)


get_obj(insights)

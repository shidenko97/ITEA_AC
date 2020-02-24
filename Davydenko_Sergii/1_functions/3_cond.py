from hw_start import insights
from Remove_unused import OBJ_KEY

# Done


def get_all_insobj(insights):
    result_bj = []

    if isinstance(insights, dict):

        for key, value in insights.items():
            if key == OBJ_KEY:
                result_bj.append(key)
                return print(f"{result_bj}")  # HOW can do _1, _2 ... >??????
            else:
                get_all_insobj(value)

    elif isinstance(insights, list):
        for insight in insights:
            get_all_insobj(insight)


get_all_insobj(insights)

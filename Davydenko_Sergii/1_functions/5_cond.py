from hw_start import insights
from Remove_unused import CAM_ID


# Done

# five cond, get all unique insights objectives
def all_uniq(insights):
    result = []
    result1 = {}

    if isinstance(insights, dict):
        for key, value in insights.items():
            if key == CAM_ID:
                result1[key] = value
                result.append(result1)
                return print(result1)
            else:
                all_uniq(value)

    elif isinstance(insights, list):
        for insight in insights:
            all_uniq(insight)
        # fife_cond(insight for insight in insights)


all_uniq(insights)

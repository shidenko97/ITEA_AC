from hw_start import insights
from Remove_unused import cam_id
# Done


def fife_cond(insights):
    result = []
    result1 = {}

    if isinstance(insights, dict):
        for key, value in insights.items():
            if key == cam_id:
                result1[key] = value
                result.append(result1)
                return print(result1)
            else:
                fife_cond(value)

    elif isinstance(insights, list):
        for insight in insights:
            fife_cond(insight)
        # fife_cond(insight for insight in insights)


fife_cond(insights)

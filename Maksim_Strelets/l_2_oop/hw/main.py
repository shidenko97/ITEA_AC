from Maksim_Strelets.l_2_oop.hw.Insight import *
from Yurii_Khomych.l_1_functions.hw_start import insights


def chooser(api):
    return {
        1: FacebookInsight,
        2: GoogleInsight,
        3: TwitterInsight,
        4: SnapchatInsight
    }[api]


def insight_builder(insight_list):
    res = []
    for el in insight_list:
        if "api" in el.keys():
            res.append(chooser(el["api"])(**el))
    return res


a = insight_builder(insights)
pass

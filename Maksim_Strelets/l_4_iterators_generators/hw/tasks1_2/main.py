from Maksim_Strelets.l_4_iterators_generators.hw.tasks1_2.network_dependent_insights import *
from Yurii_Khomych.l_1_functions.hw_start import insights


def insight_chooser(api):
    return {
        1: FacebookInsight,
        2: GoogleInsight,
        3: TwitterInsight,
        4: SnapchatInsight
    }[api]


def insight_builder(insight_list):
    res = []
    for insight in insight_list:
        if "api" in insight.keys():
            res.append(insight_chooser(insight["api"])(**insight))
    return res


a = insight_builder(insights)


pass

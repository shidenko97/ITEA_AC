from Salvador_Sakho.l_2_oop.Home_work.hw_start import insights
from Salvador_Sakho.l_2_oop.Home_work.Classes.BaseInsight_class import \
    BaseInsight
from Salvador_Sakho.l_2_oop.Home_work.Classes.API_classes import \
    GoogleInsight, FacebookInsight, SnapchatInsight, TwitterInsight
from collections import defaultdict

from Salvador_Sakho.l_2_oop.Home_work.insight_builder import insight_builder


def task_1():
    insight_dict = defaultdict(list)
    for insight in insights:
        if 'api' in insight.keys():
            insight_dict[insight['api']].append(BaseInsight(**insight))
    return insight_dict


def task_2():
    insight_dict = defaultdict(list)
    for insight in insights:
        if 'api' in insight.keys():
            insight_object = {
                1: lambda: FacebookInsight(**insight),
                2: lambda: GoogleInsight(**insight),
                3: lambda: TwitterInsight(**insight),
                4: lambda: SnapchatInsight(**insight)
            }[insight['api']]()
            insight_dict[insight['api']].append(insight_object)
    return insight_dict


def task_3():
    insight_attributes = defaultdict(list)
    for insight in insights:
        if 'api' in insight.keys():
            insight_attributes[insight['api']].append(
                insight_builder(**insight)
            )
    return insight_attributes


if __name__ == '__main__':
    base_insight_objects_list = task_1()
    insights_class_objects_list = task_2()
    insight_attr_list = task_3()

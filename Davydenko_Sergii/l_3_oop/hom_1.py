from hw_start import insights
from Davydenko_Sergii.l_3_oop import BaseInsight
from copy import deepcopy


def ch_api(insights):

    return {
        1: 'Facebookinsight',
        2: 'GoogleInsight',
        3: 'Twitterinsight',
    }




    # for insight in insights:
    #     cops = {}
    #     if 'api' in insight:
    #         cops = deepcopy(insight)
    #
    #         if insight['api'] == 1:
    #             cops['api'] = 12
    #         elif insight['api'] == 2:
    #             cops['api'] = 7
    #         elif insight['api'] == 3:
    #             cops['api'] = 10
    #         else:
    #             cops['api'] = 30
    #
    # return cops

print(ch_api(insights))

from Salvador_Sakho.l_2_oop.Home_work.Classes.BaseInsight_class import \
    BaseInsight

from Salvador_Sakho.l_2_oop.Home_work.Classes.API_classes import \
    FacebookInsight, GoogleInsight, TwitterInsight, SnapchatInsight


if __name__ == '__main__':
    base_insight = BaseInsight()
    base_insight.check_api_value()
    print(base_insight.get_metrics()['cpc'][0].get_metric())

    facebook_insight = FacebookInsight()
    for data in facebook_insight.get_insight():
        print(data)

    print(facebook_insight.insight_builder(['dimensions', 'dimensions_dict']))

    # google_insight = GoogleInsight()
    # for data in google_insight.get_insight():
    #     print(data)

    # twitter_insight = TwitterInsight()
    # for data in twitter_insight.get_insight():
    #     print(data)

    # snapchat_insight = SnapchatInsight()
    # for data in snapchat_insight.get_insight():
    #     print(data)

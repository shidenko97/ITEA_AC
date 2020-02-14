from Salvador_Sakho.l_2_oop.Home_work.Classes.API_classes import \
    FacebookInsight, GoogleInsight, TwitterInsight, SnapchatInsight


def insight_builder(**kwargs):
    result = {
        1: lambda: [
            kwargs[attribute] for attribute in [
                attribute for attribute in dir(FacebookInsight(**kwargs))
                if attribute.find('__') == -1
            ]
            if attribute in kwargs
        ],
        2: lambda: [
            kwargs[attribute] for attribute in [
                attribute for attribute in dir(GoogleInsight(**kwargs))
                if attribute.find('__') == -1
            ]
            if attribute in kwargs
        ],
        3: lambda: [
            kwargs[attribute] for attribute in [
                attribute for attribute in dir(TwitterInsight(**kwargs))
                if attribute.find('__') == -1
            ]
            if attribute in kwargs
        ]
        , 4: lambda: [
            kwargs[attribute] for attribute in [
                attribute for attribute in dir(SnapchatInsight(**kwargs))
                if attribute.find('__') == -1
            ]
            if attribute in kwargs
        ]
    }[kwargs['api']]()
    return result

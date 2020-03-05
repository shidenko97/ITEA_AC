from Salvador_Sakho.l_2_oop.Home_work.Classes.API_classes import \
    FacebookInsight, GoogleInsight, TwitterInsight, SnapchatInsight


def get_insight_class(**kwargs):
    return {
        1: lambda: FacebookInsight(**kwargs),
        2: lambda: GoogleInsight(**kwargs),
        3: lambda: TwitterInsight(**kwargs),
        4: lambda: SnapchatInsight(**kwargs)
    }[kwargs['api']]()


def insight_builder(**kwargs):
    result = [
        kwargs[attribute] for attribute in [
            attribute for attribute in
            dir(get_insight_class(**kwargs))
            if attribute.find('__') == -1]
        if attribute in kwargs
    ]
    return result

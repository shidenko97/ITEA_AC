from BaseInsight import BaseInsight
from hw_start import insights
from Google import GoogleInsight, FacebookInsight, TwitterInsight, SnapchatInsight


def search_change_api(api):
    return {
        1: FacebookInsight,
        2: GoogleInsight,
        3: TwitterInsight,
        4: SnapchatInsight,
    }.get(api, BaseInsight)


for insight in insights:
    ap = insight['api'] if 'api' in insight else None
    aps = search_change_api(ap)
    print(f'{aps.__name__}', end=' ')

    try:
        apisnik = aps(**insight)
    except ValueError as error:
        pass
    else:
        print(apisnik.__dict__)

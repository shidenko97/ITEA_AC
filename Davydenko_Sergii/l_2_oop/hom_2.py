from BaseInsight import BaseInsight
from hw_start import insights
from Google import *


def each_api(api):
    return {
        1: FacebookInsight,
        2: GoogleInsight,
        3: TwitterInsight,
        4: SnapchatInsight,
    }.get(api, BaseInsight)


for insight in insights:
    ap = insight['api'] if 'api' in insight else None
    aps = each_api(ap)
    print(f'{aps.__name__}', end=' ')

    try:
        apisnik = aps(**insight)
    except ValueError as error:
        print(f"Error 1: {error}")
    else:
        print(apisnik.__dict__)

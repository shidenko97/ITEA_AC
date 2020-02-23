from Serhii_Hidenko.l_5_modules.insights_preprocessing.base_insight import (
    BaseInsight,
)
from Serhii_Hidenko.l_5_modules.insights_preprocessing.facebook_insight import (
    FacebookInsight,
)
from Serhii_Hidenko.l_5_modules.insights_preprocessing.google_insight import (
    GoogleInsight,
)
from Serhii_Hidenko.l_5_modules.insights_preprocessing.snapchat_insight import (
    SnapchatInsight,
)
from Serhii_Hidenko.l_5_modules.insights_preprocessing.twitter_insight import (
    TwitterInsight,
)
from Serhii_Hidenko.source.hw_start import insights


def get_class_for_insight(api=None) -> BaseInsight:
    """
    Get class for insight object by `api` parameter
    :param api: Api of insight
    :type api: int
    :return: Class for insight instance
    :rtype: BaseInsight
    """

    return {
        1: FacebookInsight,
        2: GoogleInsight,
        3: TwitterInsight,
        4: SnapchatInsight,
    }.get(api, BaseInsight)


if __name__ == "__main__":

    for insight in insights:

        api_value = insight["api"] if "api" in insight else None

        insight_class = get_class_for_insight(api_value)

        try:
            bi = insight_class(**insight)
        except ValueError as err:
            print(f"Error: {err}")
        else:
            print(bi.__dict__)

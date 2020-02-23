import logging
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.base_insight import (
    BaseInsight,
)
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.facebook_insight import (
    FacebookInsight,
)
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.google_insight import (
    GoogleInsight,
)
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.snapchat_insight import (
    SnapchatInsight,
)
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.twitter_insight import (
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

    logging.basicConfig(
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )

    for insight in insights:

        if "name" in insight:
            logging.info(f"Processing insight {insight['name']}")

        api_value = insight["api"] if "api" in insight else None

        logging.debug(f"Setting `api_value` = {api_value}")

        insight_class = get_class_for_insight(api_value)

        try:
            bi = insight_class(**{**insight, **{"logger": logging}})
        except ValueError as err:
            logging.exception(f"Error: {err}")
        else:
            logging.info(bi.__dict__)

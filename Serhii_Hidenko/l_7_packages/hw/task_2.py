import pytest
from Serhii_Hidenko.l_7_packages.hw.task_1 import get_class_for_insight
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.base_insight import BaseInsight
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.facebook_insight import FacebookInsight
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.google_insight import GoogleInsight
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.twitter_insight import TwitterInsight
from Serhii_Hidenko.l_7_packages.hw.insights_preprocessing.snapchat_insight import SnapchatInsight


PARAMS_FOR_API_TESTING = [-1, 0, 1, 2, 3, 4, 5, "", None, True]
PARAMS_FOR_SUM_METRICS_TESTING = [
    {"test1": {
        "metric": 31,
        "metric_level": 88,
        "metric_average": -5,
    }},
    {"test2": {
        "metric": 30,
        "metric_level": 1,
        "metric_average": 0,
    }},
    {"test3": {
        "metric": 31,
        "metric_average": 8,
    }},
    {"test4": {
        "metric": 99,
    }},
    {"test5": {
        "metric": 99,
        "metric_level": 999,
        "metric_average": 9999,
    }},
]
PARAMS_EQ_PARAMS = [
    {
        "api": 1,
        "objective": "gg",
        "id": 14
    },
    {
        "api": 2,
        "objective": "test",
        "id": 5432
    },
    {
        "api": 3,
        "objective": "",
        "id": "235"
    },
]


@pytest.fixture(params=PARAMS_FOR_API_TESTING)
def api_param_fixture(request):

    return request.param, {
        1: FacebookInsight,
        2: GoogleInsight,
        3: TwitterInsight,
        4: SnapchatInsight
    }.get(request.param, BaseInsight)


@pytest.fixture(params=PARAMS_FOR_SUM_METRICS_TESTING)
def metrics_sum_fixture(request):

    summary = 0

    for metric in request.param.values():

        if metric["metric"] > 30:

            summary += sum(metric.values())

    return request.param, summary


@pytest.fixture(params=PARAMS_EQ_PARAMS)
def insight_eq_fixture(request):

    return request.param, BaseInsight.from_dict(request.param)


def test_get_class_for_insight(api_param_fixture):

    assert type(get_class_for_insight(api_param_fixture[0])) == type(api_param_fixture[1])


def test_sum_of_insight_metrics(metrics_sum_fixture):

    bi = BaseInsight(api=1, metric_summary=metrics_sum_fixture[0])

    assert metrics_sum_fixture[1] == bi.calculate_sum_of_all_metrics()


def test_get_insight_attribute():

    bi = BaseInsight(api=2)

    assert bi.api == bi.get_attribute_by_name("api")


def test_get_reportname_uppercase():
    bi = BaseInsight(api=1, report_name="Test reportname")

    assert bi.get_report_name_uppercase() == bi.report_name.upper()


def test_insight_eq(insight_eq_fixture):

    assert BaseInsight(**insight_eq_fixture[0]) == insight_eq_fixture[1]

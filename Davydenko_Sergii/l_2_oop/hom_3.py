from hw_start import insights
import copy


def insight_builder(insights):
    # search only needed keys
    # make copy of each Insight and create each insight
    m_keys = (
        "metric_name", "api", "report_name", "objective",
        "unit", "currency", "id", "validator_insight_type"
              )
    all_keys = {}
    cop = []

    if isinstance(insights, dict):
        if 'metric_name' in insights.keys():
            for key, value in insights.items():
                if key in m_keys:
                    all_keys[key] = value
                    cop = copy.deepcopy(all_keys)
            return print(cop)

    elif isinstance(insights, list):
        for insight in insights:
            insight_builder(insight)


insight_builder(insights)

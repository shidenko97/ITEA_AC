from Salvador_Sakho.l_2_oop.Home_work import insight_builder
from Salvador_Sakho.l_2_oop.Home_work.Classes.API_classes import \
    FacebookInsight, GoogleInsight
from Salvador_Sakho.l_2_oop.Home_work.Classes.BaseInsight_class import \
    BaseInsight

if __name__ == '__main__':
    base_insight = BaseInsight('cpc', 1, 'device', 'Conversions', 'EUR', 'EUR',
                               '6156696417772'
                               , 'Same money - more results')
    metric_summary = base_insight.metric_summary_init(
        metric_summary={'metric': '1', 'metric_level': '1',
                        'metric_average': '1', 'is_outlier': '1'
            , 'true_sign': '1', 'sign': '1', 'mark': '1', 'unit': '1'
            , 'metric_name_frontend': '1', 'mark_key': '1'
            , 'metric_name_frontend_key': '1', 'unit_key': '1'}
    )

    facebook_insight = FacebookInsight(
        'cpc', 1, 'device', 'Conversions', 'EUR', 'EUR', '6156696417772'
        , 'Same money - more results'
        , dimensions_dict={
            'adset_id': ["6145264569772"]
            , 'campaign_id': ["6145264558972"]
        }
        , dimensions={
            "name": "dimension:age"
            , "value": "18-24"
            , "value_raw": "18-24"
            , "name_key": "age",
        }
    )
    google_insight = GoogleInsight('cpc', 1, 'device', 'Conversions', 'EUR',
                                   'EUR', '6156696417772'
                                   , 'Same money - more results',
                                   actions="create_new_entity")

    insight_builder.insight_builder(1, 'cpc', 1, 'device', 'Conversions',
                                    'EUR', 'EUR',
                                    '6156696417772'
                                    , 'Same money - more results')

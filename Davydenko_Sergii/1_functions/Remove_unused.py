# 1. Remove unused keys from insight like:
# * On root level remove:
# from all_in import *

root_keys = ['period', 'count', 'total_count', 'page_id']


# On entities_affected -> entities level remove:

entiti_keys_to_del = ['link', 'status', 'days_in_data']
entiti_keys = ['entities_affected', 'entities']


# Remove keys which not fit the condition
#     * Remove each element from "table_columns" where "unit" not equal to "EUR"
    # * Remove each element from "metric_sums" where "unit_key" not equal to "EUR"

unit_keys = ['unit', 'unit_key']


# 3. Get all insights objectives into list of strings result: `["objective_1", "objective_2"]`

obj_key = 'objective'


# 4. Get all insights objectives into dict result:
# [{"objective": "objective_1"}, {"objective": "objective_2"},]

obj_dict = 'objective'


# 5. Get all insights campaign_id into dict result:
# [{"campaign_id": "123"}, {"campaign_id": "113"},]

cam_id = 'campaign_id'


# 6 . Get all unique insights objectives

uniq_key = 'objective'


# 7. Get all insights "metric_sums" and calculate sum and average for
# all elements of "metric_sums" list (sum, sum_level, sum_general)
# result:{ "all_sum": sum of all insights of (sum, sum_level, sum_general)
# metric sums "all_average": average of all insights of (sum, sum_level, sum_general)
# metric sums }

metr_sums = 'metric_sums'
metr_list = ['sum', 'sum_level', 'sum_general']


# 8 Sort list of insights by "type", "api", "report_name" and "objective"

sort_key = ['type', 'api', 'report_name', 'objective']


# 11. Calculate summary by formulas (if root "period" > 4 or None
# set default root "period" as 7):

col_sum = 'metric_sums'
sum_cond = ['sum', 'sum_level', 'sum_general']

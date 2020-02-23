# 1. Remove unused keys from insight like:
# * On root level remove:
# from all_in import *

ROOT_KEYS = ["period", "count", "total_count", "page_id"]


# On entities_affected -> entities level remove:

ENTITI_KEYS_TO_DEL = ["link", "status", "days_in_data"]
ENTITI_KEYS = ["entities_affected", "entities"]


# Remove keys which not fit the condition
#     * Remove each element from "table_columns" where "unit" not equal to "EUR"
# * Remove each element from "metric_sums" where "unit_key" not equal to "EUR"

UNIT_KEYS = ["unit", "unit_key"]


# 3. Get all insights objectives into list of strings result: `["objective_1", "objective_2"]`

OBJ_KEY = "objective"


# 4. Get all insights objectives into dict result:
# [{"objective": "objective_1"}, {"objective": "objective_2"},]

OBJ_DICT = "objective"


# 5. Get all insights campaign_id into dict result:
# [{"campaign_id": "123"}, {"campaign_id": "113"},]

CAM_ID = "campaign_id"


# 6 . Get all unique insights objectives

UNIQ_KEY = "objective"


# 7. Get all insights "metric_sums" and calculate sum and average for
# all elements of "metric_sums" list (sum, sum_level, sum_general)
# result:{ "all_sum": sum of all insights of (sum, sum_level, sum_general)
# metric sums "all_average": average of all insights of (sum, sum_level, sum_general)
# metric sums }

METR_SUMS = "metric_sums"
METR_LIST = ["sum", "sum_level", "sum_general"]


# 8 Sort list of insights by "type", "api", "report_name" and "objective"

SORT_KEY = ["type", "api", "report_name", "objective"]


# 11. Calculate summary by formulas (if root "period" > 4 or None
# set default root "period" as 7):

COL_SUM = "metric_sums"
SUM_COND = ["sum", "sum_level", "sum_general"]

from hw.hw_start import insights
from hw.functions import *

removable = ["period", "count", "total_count", "page_id", "entities_affected.entities.link",
             "entities_affected.entities.status", "entities_affected.entities.days_in_data"]

# task 1
# for el in removable:
#     dict_remove(insights, el)

# tasks 2, 9, 10
# dfs(insights)

# task 3
# temp = dict_get(insights, "objective")

# task 4
# temp = ins_to_dict(insights, "objective")

# task 5


# task 6
# temp = list(set(ins_to_str(insights)))

# task 7
# sum = calculate(insights, "metric_sums.sum")
# sum_level = calculate(insights, "metric_sums.sum_level")
# sum_general = calculate(insights, "metric_sums.sum_general")

# task 8
# insights = sort(insights, "type")
# insights = sort(insights, "api")
# insights = sort(insights, "report_name")
# insights = sort(insights, "objective")

save(insights)
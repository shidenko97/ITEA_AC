import Salvador_Sakho.l_1_functions.Home_work.action_handler as action_handler
from Salvador_Sakho.l_1_functions.hw_start import insights

if __name__ == "__main__":
    # remove_key
    # entities_to_list -> check entities_spend_sum ???
    # to_dict -> check main_dict
    # to_list -> check main_list
    # to_set -> check main_set
    # objective_case -> check main_set
    # campaign_id -> check main_dict
    # metric_sums_case -> will print result for all metrics
    # report_name_case -> check main_dict
    # page_id_case -> check main_dict
    # sort_by_keys_case -> check main_dict
    # calculate_summary_case -> will print result

    ah = action_handler.HandleAction()
    print(
        ah.run_process(
            [line for line in insights], action="calculate_summary_case"
        )
    )

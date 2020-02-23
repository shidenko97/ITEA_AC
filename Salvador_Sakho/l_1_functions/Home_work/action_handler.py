from Salvador_Sakho.l_1_functions.Home_work.general_scripts import (
    MainApplicationLogicClass,
)


class HandleAction(MainApplicationLogicClass):
    def run_process(self, data, action=None):
        if action == "page_id_case":
            self._page_id_case_handler(data)
        elif action == "metric_sums_case":
            self._metric_sums_case_handler(data)
        elif action == "report_name_case":
            self._report_name_case_handler(data)
        elif action == "objective_case":
            self._unique_objective_case_handler(data)
        elif action == "campaign_id":
            self._campaign_id_case_handler(data)
        elif action == "sort_by_keys_case":
            self._sort_by_keys_insights_list(data)
        elif action == "calculate_summary_case":
            return self._calculate_summary_case_handler(data)
        elif action in [
            "remove_key",
            "entities_to_list",
            "to_dict",
            "to_list",
            "to_set",
        ]:
            if isinstance(data, dict):
                self._handle_dict_data(data.values(), action=action)
            if isinstance(data, list):
                self._handle_list_data(data, action=action)

from copy import copy
from functools import reduce


class MainApplicationLogicClass:
    def __init__(self):
        self.main_list = []
        self.main_dict = {}
        self.general_id = 0
        self.campaign_id_dict = {"campaign_id": []}
        self.main_set = set()
        self.entities_spend_sum = []
        self.keys_for_remove = (
            "period",
            "count",
            "total_count",
            "page_id",
            "link",
            "status",
            "days_in_data",
            ("table_columns", "unit", "EUR"),
            ("metric_sums", "unit_key", "EUR"),
        )

    def _handle_list_data(
        self, list_data, key=None, action=None, **collection
    ):
        for data in list_data:
            if isinstance(data, dict):
                self._handle_dict_data(
                    data, collection=collection, action=action
                )
            elif isinstance(data, list):
                self._handle_list_data(
                    data, key=key, collection=collection, action=action
                )
            else:
                self._handle_action(
                    collection, key=key, value=data, action=action
                )

    def _handle_dict_data(self, dictionary, action=None, **collection):
        temp_dict = copy(dictionary)
        for key, val in temp_dict.items():
            self._check_key(dictionary, key, action)
            if isinstance(val, dict):
                self._handle_dict_data(
                    val, collection=collection, action=action
                )
            elif isinstance(val, list):
                self._handle_list_data(
                    val, key=key, main_list=collection, action=action
                )
            else:
                self._handle_action(
                    collection=dictionary, key=key, value=val, action=action
                )

    def _check_key(self, collection, key, action):
        if key in collection.keys():
            if (
                (key in self.keys_for_remove[1:7])
                or (
                    key
                    in [self.keys_for_remove[7][1], self.keys_for_remove[8][1]]
                    and collection[key] != "EUR"
                )
            ) and action == "remove_key":
                self.remove_by_key(collection, key)
            if (
                key in [self.keys_for_remove[7][0], self.keys_for_remove[8][0]]
                and action == "remove_key"
            ):
                if isinstance(collection[key], dict):
                    self.handle_dict_data(
                        collection[key].values(), action=action
                    )
                if isinstance(collection[key], list):
                    self.handle_list_data(collection[key], action=action)
            if key == "entities" and action == "entities_to_list":
                self._entities_key_case_handler(collection)
        return collection

    def _to_dict(self, key, val):
        if key in self.main_dict.keys():
            self.main_dict[key].append(val if val is not None else None)
        else:
            self.main_dict[key] = [val if val is not None else None]

    def _to_list(self, *data):
        self.main_list.append(data[0])

    def _handle_action(self, collection, key=None, value=None, action=None):
        if action in ["remove_key", "entities_to_list"]:
            self._check_key(collection, key, action)
        elif action == "to_dict":
            self._to_dict(key, value)
        elif action == "to_list":
            self._to_list([str(key), str(value)])
        elif action == "to_set":
            self.main_set.add((key, value))
        else:
            raise Exception(f"Unexpected type of action: {action}")

    def _remove_by_key(self, collection, key_val):
        with open("./keys_removed_log_file.txt", "a+") as log_file:
            log_file.write(
                f"Removed key:{key_val}\n Collection{collection}\n******\n"
            )
            if isinstance(collection, dict):
                if key_val in collection.keys():
                    del collection[key_val]
            if isinstance(collection, list):
                collection.remove(key_val)
        return collection

    def _entities_key_case_handler(self, collection):
        for data in collection["entities"]:
            if data["spend_sum"] > 200:
                self.entities_spend_sum.append(data)

    def _unique_objective_case_handler(self, list_comp):
        self._handle_list_data(
            list_comp, main_dict=self.main_dict, action="to_dict"
        )
        for data in self.main_dict["objective"]:
            self.main_set.add(data)

    def _campaign_id_case_handler(self, list_comp):
        self._handle_list_data(
            list_comp, main_dict=self.main_dict, action="to_dict"
        )
        self.main_dict = self.main_dict["campaign_id"]

    def _metric_sums_case_handler(self, list_comp):
        self._handle_list_data(
            list_comp, main_dict=self.main_dict, action="to_dict"
        )
        dict_sum = self.main_dict["sum"]
        dict_sum_level = self.main_dict["sum_level"]
        dict_sum_general = self.main_dict["sum_general"]
        self._continuing_calculations(
            dict_sum,
            dict_sum_level,
            dict_sum_general,
            sum_funk=self.sum_funk,
            avg_funk=self.avg_funk,
        )

    def _continuing_calculations(self, *args, **continuing_func_to_perform):
        for data in args:
            continuing_func_to_perform["avg_funk"](
                continuing_func_to_perform["sum_funk"](data), len(data)
            )

    def _avg_funk(self, value, data_len):
        print(f"AVG of values: {value / data_len}")
        return value / data_len

    def _sum_funk(self, *data):
        print(f"Sum of values: {reduce(lambda a, b: a + b, data[0])}")
        return reduce(lambda a, b: a + b, data[0])

    def _report_name_case_handler(self, list_comp):
        self._handle_list_data(
            list_comp, main_dict=self.main_dict, action="to_dict"
        )
        for idx, data in enumerate(self.main_dict["report_name"]):
            if data == "device":
                self.main_dict["report_name"][idx] = data.upper()
        return self.main_dict

    def _page_id_case_handler(self, list_comp):
        self._handle_list_data(
            list_comp, main_dict=self.main_dict, action="to_dict"
        )
        for idx, data in enumerate(self.main_dict["page_id"]):
            if data == "(not set)":
                self.main_dict["page_id"][idx] = None
        return self.main_dict

    def _sort_by_keys_insights_list(self, list_comp):
        self._handle_list_data(
            list_comp, main_dict=self.main_dict, action="to_dict"
        )
        # "type", "api", "report_name" and "objective"
        new_dict = {
            "type": self.main_dict["type"],
            "api": self.main_dict["api"],
            "report_name": self.main_dict["report_name"],
            "objective": self.main_dict["objective"],
        }

        for key, val in self.main_dict.items():
            if key not in ["type", "api", "report_name", "objective"]:
                new_dict[key] = self.main_dict[key]
        self.main_dict = new_dict
        return self.main_dict

    def _calculate_summary_case_handler(self, list_comp):
        results = []
        for collection in list_comp:
            if "api" in collection.keys():
                period = collection["period"]
                for data in collection["metric_sums"]:
                    function_calculations_result = {
                        1: lambda: data["sum"] * data["sum_level"] / 1
                        if data["sum_general"] == 0
                        else data["sum_general"] / 7
                        if period is None or period > 4
                        else period,
                        2: lambda: data["sum"] * data["sum_level"] ** 2 / 1
                        if data["sum_general"] == 0
                        else data["sum_general"] / 7
                        if period is None or period > 4
                        else period,
                        3: lambda: data["sum_level"] / 1
                        if data["sum_general"] == 0
                        else data["sum_general"] / 7
                        if period is None or period > 4
                        else period,
                        4: lambda: data["sum_level"]
                        * data["sum_general"]
                        / 100
                        / 7
                        if period is None or period > 4
                        else period,
                    }[collection["api"]]()
                    results.append(function_calculations_result)
        return results

from abc import ABCMeta, abstractmethod


class AbstractInsight(metaclass=ABCMeta):
    """Abstract class for Insight"""

    @abstractmethod
    def _check_api_is_correct(self):
        pass

    @abstractmethod
    def calculate_sum_of_all_metrics(self):
        pass

    @abstractmethod
    def get_attribute_by_name(self, name):
        pass

    @abstractmethod
    def print_attribute_by_name(self, name):
        pass

    @abstractmethod
    def get_report_name_uppercase(self, name):
        pass

    @abstractmethod
    def _create_metrics(metrics):
        pass

from Serhii_Hidenko.l_3_oop.hw.metricsummary import MetricSummary
from Serhii_Hidenko.l_3_oop.hw.abstractinsight import AbstractInsight
from Serhii_Hidenko.l_3_oop.hw.decorators import (
    execution_time_and_result_decorator,
)


class BaseInsight(AbstractInsight):
    """Base class for insight"""

    def __init__(
        self,
        metric_name=None,
        api=None,
        report_name=None,
        objective=None,
        unit=None,
        currency=None,
        validator_insight_type=None,
        metric_summary=None,
        **kwargs,
    ):

        self.api = api

        # Check is api a correctly
        self._check_api_is_correct()

        self.metric_name = metric_name
        self.report_name = report_name
        self.objective = objective
        self.__unit = unit
        self.__currency = currency
        self.id = kwargs["id"] if "id" in kwargs else None
        self.validator_insight_type = validator_insight_type

        # Create dict of metrics
        self.metrics = self._create_metrics(metric_summary)

    @property
    def currency(self):
        """Getter for `currency` attribute"""

        print(self.__currency)

        return self.__currency

    @property
    def unit(self):
        """Getter for `unit` attribute"""

        print(self.__unit)

        return self.__unit

    @property
    def print(self):
        """Getter for `print` attribute"""

        return "print"

    @property
    @execution_time_and_result_decorator(filename="functions_executions.txt")
    def api_name(self):
        """Get network name"""

        return __class__.__name__.replace("Insight", "")

    @execution_time_and_result_decorator(filename="functions_executions.txt")
    def _check_api_is_correct(self):
        """Check is api attribute a valid value"""

        valid_values = (1, 2, 3, 4)

        if self.api not in valid_values:
            raise ValueError(f"Incorrect value [{self.api}] for attribute api")

    @execution_time_and_result_decorator(filename="functions_executions.txt")
    def calculate_sum_of_all_metrics(self):
        """Calculate sum of all metrics instances"""

        sum = 0

        for key, metric in self.metrics.items():

            if metric.metric > 30:
                sum += metric.calculate_sum_of_all_attributes()

        return sum

    def get_attribute_by_name(self, name):
        """Getting attribute of class by name"""

        try:
            return getattr(self, name)
        except AttributeError as err:
            return err

    def print_attribute_by_name(self, name):
        """Printing attribute of class by name"""

        print(self.get_attribute_by_name(name))

    def get_report_name_uppercase(self):
        """Get `report_name` attribute in uppercase"""

        return self.report_name.upper()

    @staticmethod
    def _create_metrics(metrics) -> dict:
        """
        Filter the values in metrics dict and replace it on MetricSummary instances
        :param metrics: List of dict where each element is some metric
        :type metrics: list
        :return: Dict of MetricSummary instances
        :rtype: dict
        """

        if not isinstance(metrics, dict):
            return {}

        metric_attributes = [
            attr
            for attr in dir(MetricSummary())
            if not attr.startswith("__")
            and not attr.endswith("__")
            and not attr.startswith("_")
        ]

        for key, params in metrics.items():
            metrics[key] = MetricSummary(
                **dict(
                    filter(
                        lambda param: param[0] in metric_attributes,
                        params.items(),
                    )
                )
            )

        return metrics

    def __eq__(self, other):
        """
        Re-declaring standard __eq__ function to comparing hashes of tuple (api, objective, id)
        :param other: Another object to compare
        :type other: BaseInsight
        :return: Result of comparing
        :rtype: bool
        """

        if not isinstance(other, BaseInsight):
            return False

        return hash((self.api, self.objective, self.id)) == hash(
            (other.api, other.objective, other.id)
        )

    def __len__(self):
        """Re-declare __len__ magic method by len of metric attribute"""

        return len(self.metrics)

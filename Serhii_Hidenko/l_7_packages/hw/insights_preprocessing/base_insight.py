from Serhii_Hidenko.l_4_iterators_generators.hw.metricsummary import MetricSummary


class BaseInsight:
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
            logger=None,
            **kwargs
    ):

        self.logger = logger

        self.print_log("Start __init__")
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
        self.print_log("Finish __init__")

    def print_log(self, msg=""):

        if self.logger is not None:
            self.logger.info(msg)

    @property
    def currency(self):
        """Getter for `currency` attribute"""

        self.print_log("Property currency")

        return self.__currency

    @property
    def unit(self):
        """Getter for `unit` attribute"""

        self.print_log("Property unit")

        return self.__unit

    @property
    def print(self):
        """Getter for `print` attribute"""

        self.print_log("Property print")

        return "print"

    @property
    def api_name(self):
        """Get network name"""

        self.print_log("Property api_name")

        return __class__.__name__.replace("Insight", "")

    def _check_api_is_correct(self):
        """Check is api attribute a valid value"""

        self.print_log("Check is api correct")

        valid_values = (1, 2, 3, 4)

        if self.api not in valid_values:
            raise ValueError(f"Incorrect value [{self.api}] for attribute api")

    def calculate_sum_of_all_metrics(self):
        """Calculate sum of all metrics instances"""

        self.print_log("Calculate sums of metrics")

        sum = 0

        for key, metric in self.metrics.items():

            if metric.metric > 30:
                sum += metric.calculate_sum_of_all_attributes()

        return sum

    def get_attribute_by_name(self, name):
        """Getting attribute of class by name"""

        self.print_log("Getting attribute by name")

        try:
            return getattr(self, name)
        except AttributeError as err:
            return err

    def print_attribute_by_name(self, name):
        """Printing attribute of class by name"""

        self.print_log("Printing attribute by name")

        print(self.get_attribute_by_name(name))

    def get_report_name_uppercase(self):
        """Get `report_name` attribute in uppercase"""

        self.print_log("Getting report name in upper case")

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

        metric_attributes = [attr for attr in dir(MetricSummary()) if not attr.startswith("__")
                             and not attr.endswith("__") and not attr.startswith("_")]

        for key, params in metrics.items():
            metrics[key] = MetricSummary(**dict(filter(lambda param: param[0] in metric_attributes, params.items())))

        return metrics

    def __eq__(self, other):
        """
        Re-declaring standard __eq__ function to comparing hashes of tuple (api, objective, id)
        :param other: Another object to compare
        :type other: BaseInsight
        :return: Result of comparing
        :rtype: bool
        """

        self.print_log("Call __eq__")

        if not isinstance(other, BaseInsight):
            return False

        return hash((self.api, self.objective, self.id)) == hash((other.api, other.objective, other.id))

    def __len__(self):
        """Re-declare __len__ magic method by len of metric attribute"""

        self.print_log("Call __len__")

        return len(self.metrics)

    def to_dict(self) -> dict:
        """
        Return a dict of class attributes
        :return: Dict of class attributes
        :rtype: dict
        """

        self.print_log("Call to_dict")

        return self.__dict__

    @classmethod
    def from_dict(cls, attributes):
        """
        Return a class instance with attributes from dict
        :param attributes: Attributes for class instance
        :type attributes: dict
        :return: Instance of class
        :rtype: BaseInsight
        """

        return cls(**attributes)

    def __getitem__(self, item):
        """Get metric of instance by key"""

        self.print_log("Call __getitem__")

        return self.metrics[item]

    def __setitem__(self, key, value):
        """Set metric in instance by key"""

        self.print_log("Call __setitem__")

        self.metrics[key] = value

    def __delitem__(self, key):
        """Del metric from instance by key"""

        self.print_log("Call __delitem__")

        del self.metrics[key]

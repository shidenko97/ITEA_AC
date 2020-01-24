from Serhii_Hidenko.l_2_oop.hw.metricsummary import MetricSummary


class BaseInsight:

    def __init__(self, metric_name=None, api=None, report_name=None, objective=None, unit=None, currency=None,
                 validator_insight_type=None, metric_summary=None, **kwargs):

        self.metric_name = metric_name
        self.api = api
        self.report_name = report_name
        self.objective = objective
        self.unit = unit
        self.currency = currency
        self.id = kwargs["id"] if "id" in kwargs else None
        self.validator_insight_type = validator_insight_type

        # Check is api a correctly
        self._check_api_is_correct()

        # Create dict of metrics
        self._create_metrics(metric_summary)

    def _check_api_is_correct(self):
        """Check is api attribute a valid value"""

        valid_values = (1, 2, 3, 4)

        if self.api not in valid_values:
            raise ValueError(f"Incorrect value [{self.api}] for attribute api")

    def _create_metrics(self, metrics):
        """
        Set dict of metrics by insight dict
        :param metrics: List of dict where each element is some metric
        :type metrics: list
        """

        if not isinstance(metrics, dict):
            self.metrics = {}
        else:
            self.metrics = {metric_key: MetricSummary(**metric_params) for metric_key, metric_params in metrics.items()}

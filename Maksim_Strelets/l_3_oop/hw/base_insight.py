import functools
import time
from functools import total_ordering
from Maksim_Strelets.l_3_oop.hw.metric_summary import MetricSummary
from Maksim_Strelets.l_3_oop.hw.abstract_insight import *


# hw 3 task 5
def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        res = f"Finished {func.__name__!r} in {run_time:.7f} secs with result {value}\n"
        with open("log.txt", "a+") as f:
            f.write(res)
            pass

    return wrapper_timer


@total_ordering
class BaseInsight(AbstractInsight, metaclass=MergedMetaInsight):
    def __init__(self, metric_name=None, api=None, report_name=None,
                 objective=None, unit=None, currency=None, id=None,
                 validator_insight_type=None, **kwargs):
        self.api = api
        self.check_api()

        self.metric_name = metric_name
        self.report_name = report_name
        self.objective = objective
        self._unit = unit
        self._currency = currency
        self.id = id
        self.validator_insight_type = validator_insight_type
        self.metrics = {}

        if "metric_summary" in kwargs.keys():
            self.set_metrics(kwargs["metric_summary"])

    # hw 2 task 1
    def check_api(self):
        if self.__getattribute__("api") not in range(1, 5):
            raise KeyError("api key must be in (1, 2, 3, 4)")

    @timer
    def set_metrics(self, metric_summary):
        for key in metric_summary:
            self.metrics[key] = MetricSummary(key, **metric_summary[key])

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __gt__(self, other):
        if self.api != other.api:
            return self.api > other.api
        if self.objective != other.objective:
            return self.objective > other.objective
        return self.id > other.id

    # hw 3 task 1
    def print_values(self):
        for key, val in self.__dict__.items():
            print(key, "=", val)

    # hw 3 task 2
    @timer
    def sum_metrics(self):
        res = 0
        for metr in self.metrics.values():
            if metr.metric > 30:
                res += metr.metric
        return res

    def __len__(self):
        return len(self.metrics)

    # hw 3 task 3
    def my_get(self, name):
        return self.__getattribute__(name)

    def my_print(self, name):
        print(self.my_get(name))

    @property
    def currency(self):
        return self._currency

    @property
    def unit(self):
        return self._unit

    def upper_report_name(self):
        return self.report_name.upper()



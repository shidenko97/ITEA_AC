from abc import ABC, abstractmethod, ABCMeta
from Maksim_Strelets.l_4_iterators_generators.hw.tasks1_2.meta_insight import MetaInsight


class MergedMetaInsight(MetaInsight, ABCMeta):
    pass


class AbstractInsight(ABC):
    @abstractmethod
    def check_api(self):
        pass

    @abstractmethod
    def print_values(self):
        pass

    @abstractmethod
    def upper_report_name(self):
        pass
from Serhii_Hidenko.source.hw_start import insights
from Serhii_Hidenko.l_3_oop.hw.baseinsight import BaseInsight


if __name__ == "__main__":

    try:
        bi = BaseInsight(**insights[7])
    except ValueError as err:
        print(f"Error: {err}")
    else:
        print(bi.api_name)
        print(bi.calculate_sum_of_all_metrics())

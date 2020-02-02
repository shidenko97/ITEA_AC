from Serhii_Hidenko.l_3_oop.hw.task_1 import get_class_for_insight
from Serhii_Hidenko.source.hw_start import insights


if __name__ == "__main__":

    for insight in insights:

        api_value = insight["api"] if "api" in insight else None

        insight_class = get_class_for_insight(api_value)

        try:
            bi = insight_class(**insight)
        except ValueError as err:
            print(f"Error: {err}")
        else:
            print(bi.__dict__)

            print("Length of metrics: ")

            for name, metric in bi.metrics.items():

                print(f"\t{name}: {metric.calculate_sum_of_all_attributes()}")

            print(f"All metrics sum: {bi.calculate_sum_of_all_metrics()}")

            print(f"Len of class: {len(bi)}")

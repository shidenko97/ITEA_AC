from Serhii_Hidenko.l_5_modules.insights_preprocessing import baseinsight, task_1_from_3
from Serhii_Hidenko.source.hw_start import insights


if __name__ == "__main__":

    insights_networks_list = []

    for insight in insights:

        try:
            instance_class = task_1_from_3.get_class_for_insight(insight.get("api", None))
            bi = instance_class(**insight)
            insights_networks_list.append(bi)
        except ValueError as err:
            print(f"Error: {err}")
        else:
            print(f"{bi.__class__} {bi.__dict__}")

    print(insights_networks_list)

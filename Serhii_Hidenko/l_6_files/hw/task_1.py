import csv
import json
import os


show_condition = "all"


# Parameters for parsing of each subtask
TASKS_UTILS = [
    {
        "filename": "hw_files/analyzer/project_id-{project_id}/project_execution-{project_execution}"
                    "/2-function_name-generate_nb_insights/",
        "file_condition": lambda project_execution: lambda file: file.endswith('-1.json'),
        "open": lambda name: json.load(open(name)),
        "filter": lambda dimension, breakdowns: dimension["name"].replace("dimension:", "") in breakdowns,
        "log_text": lambda **kwargs: f"analyzer_insights_len: {kwargs['insights_len']}\n"
                                     f"analyzer_insights_with_br_len: {kwargs['insights_with_br_len']}"
    },
    {
        "filename": "hw_files/mid/",
        "file_condition": lambda project_execution: lambda file: file.startswith(f"{project_execution}"),
        "open": lambda name: csv.DictReader(open(name)),
        "filter": lambda dimension, breakdowns: dimension in breakdowns,
        "log_text": lambda **kwargs: f"mid_insights_len: {kwargs['insights_len']}\n"
                                     f"mid_insights_with_br_len: {kwargs['insights_with_br_len']}"
    },
    {
        "filename": "hw_files/final_results/",
        "file_condition": lambda project_execution: lambda file: file == f"cc_pp_{project_execution}.json",
        "open": lambda name: json.load(open(name)),
        "filter": lambda dimension, breakdowns: dimension["name"] in breakdowns,
        "log_text": lambda **kwargs: f"final_insights_len: {kwargs['insights_len']}\n"
                                     f"final_insights_with_br_len: {kwargs['insights_with_br_len']}"
    },
]


def get_directory_listing(directory, condition=None) -> str:
    """
    Returns all file in directory by condition
    :param directory: Directory for scan
    :type directory: str
    :param condition: Function for check file
    :type condition: None
    :return: Filename
    :rtype: str
    """

    with os.scandir(directory) as files:

        for file_ in files:

            if condition is not None and not condition(file_.name):
                continue

            yield file_.name


def get_count_of_insight(filename, breakdowns, task_params) -> tuple:
    """
    Returns all count of insights and counts with condition
    :param filename: File for scaning insights
    :type filename: str
    :param breakdowns: Condition words for scaning
    :type breakdowns: list
    :param task_params: Params of task
    :type task_params: dict
    :return: Tuple of two elements - all count and count with condition
    :rtype: tuple
    """

    insights_len = insights_with_br_len = 0

    for insight in task_params["open"](filename):

        if show_condition in ["all", "without-breakdowns"]:
            insights_len += 1

        if show_condition in ["all", "breakdowns"]:

            if "dimensions" not in insight:
                return insights_len, insights_with_br_len

            dimensions = insight["dimensions"]

            if isinstance(dimensions, str):
                dimensions = eval(dimensions)

            insights_with_br_len += int(
                any(
                    filter(
                        lambda dimension: task_params["filter"](dimension, breakdowns),
                        dimensions
                    )
                )
            )

    return insights_len, insights_with_br_len


def main():

    parsed_json = json.load(open("hw_files/input_data.json"))

    breakdowns = parsed_json["breakdowns"]
    project_id_to_project_execution = parsed_json["project_id_to_project_execution"]

    for project_id, project_executions in project_id_to_project_execution.items():

        for project_execution in project_executions:

            print(f"project_id: {project_id}, project_execution_id: {project_execution}")

            for task_params in TASKS_UTILS:

                directory = task_params["filename"].replace("{project_id}", str(project_id)).\
                    replace("{project_execution}", str(project_execution))

                insights_len = insights_with_br_len = 0

                for file in get_directory_listing(directory, task_params["file_condition"](project_execution)):

                    insights = get_count_of_insight(f"{directory}{file}", breakdowns, task_params)
                    insights_len += insights[0]
                    insights_with_br_len += insights[1]

                print(task_params["log_text"](insights_len=insights_len, insights_with_br_len=insights_with_br_len))

                """
                filename_task_1 = f"hw_files/analyzer/project_id-{project_id}/project_execution-{project_execution}" \
                                  f"/2-function_name-generate_nb_insights/"

                analyzer_insights_len = analyzer_insights_with_br_len = 0

                for file in get_directory_listing(filename_task_1, lambda a: a.endswith('-1.json')):

                    analyzer_insights = get_count_of_insight(f"{filename_task_1}{file}", breakdowns)
                    analyzer_insights_len += analyzer_insights[0]
                    analyzer_insights_with_br_len += analyzer_insights[1]

                print(f"analyzer_insights_len: {analyzer_insights_len}\n"
                      f"analyzer_insights_with_br_len: {analyzer_insights_with_br_len}")

            filename_task_2 = f"hw_files/mid/"

            mid_insights_len = mid_insights_with_br_len = 0

            for file in get_directory_listing(filename_task_2, lambda a: a.startswith(str(project_execution))):

                mid_insights = get_count_of_insight(f"{filename_task_2}{file}", breakdowns)
                mid_insights_len += mid_insights[0]
                mid_insights_with_br_len += mid_insights[1]

            print(f"mid_insights_len: {mid_insights_len}\n"
                  f"mid_insights_with_br_len: {mid_insights_with_br_len}")

            filename_task_3 = f"hw_files/final_results/"

            final_insights_len = final_insights_with_br_len = 0

            for file in get_directory_listing(filename_task_3, lambda a: a == f"cc_pp_{project_execution}.json"):
                final_insights = get_count_of_insight(f"{filename_task_3}{file}", breakdowns)
                final_insights_len += final_insights[0]
                final_insights_with_br_len += final_insights[1]

            print(f"final_insights_len: {final_insights_len}\n"
                  f"final_insights_with_br_len: {final_insights_with_br_len}")

            
            filename_task_3 = f"hw_files/final_results/"

            print("final_insights_len: " + str(sum([
                len(json.load(open(filename_task_3 + file)))
                for file in get_directory_listing(filename_task_3, lambda a: a == f"cc_pp_{project_execution}.json")
            ])))
            """


if __name__ == "__main__":

    main()

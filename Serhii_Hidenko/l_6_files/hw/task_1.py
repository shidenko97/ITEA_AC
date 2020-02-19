import csv
import json
import os


show_condition = "all"
output_file = None


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
                dimensions = json.loads(dimensions.replace("'", "\""))

            insights_with_br_len += int(
                any(
                    filter(
                        lambda dimension: task_params["filter"](dimension,
                                                                breakdowns),
                        dimensions
                    )
                )
            )

    return insights_len, insights_with_br_len


def get_directory_insight_len(
        directory,
        task_params,
        project_execution,
        breakdowns
) -> tuple:
    """
    Return a length of insights in directory
    :param directory: Directory for scan
    :type directory: str
    :param task_params: Parameters for the each task
    :type task_params: dict
    :param project_execution: Project execution id
    :type project_execution: str
    :param breakdowns: The breakdowns
    :type breakdowns: list
    :return: Full len and lenn with breakdowns
    :rtype: tuple
    """

    insights_len = insights_with_br_len = 0

    for file in get_directory_listing(
        directory,
        task_params["file_condition"](project_execution)
    ):
        insights = get_count_of_insight(
            f"{directory}{file}",
            breakdowns,
            task_params
        )
        insights_len += insights[0]
        insights_with_br_len += insights[1]

    return insights_len, insights_with_br_len


def main():

    if output_file is not None:
        output_file_data = []

    parsed_json = json.load(open("hw_files/input_data.json"))

    breakdowns = parsed_json["breakdowns"]
    proj_id_to_proj_exec = parsed_json["project_id_to_project_execution"]

    for project_id, project_executions in proj_id_to_proj_exec.items():

        for project_execution in project_executions:

            if output_file is not None:

                output_file_current_data = {
                    "project_id": project_id,
                    "project_execution_id": project_execution
                }

            print(f"project_id: {project_id}, "
                  f"project_execution_id: {project_execution}")

            for task_params in TASKS_UTILS:

                directory = task_params["filename"].\
                    replace("{project_id}", str(project_id)).\
                    replace("{project_execution}", str(project_execution))

                insights_len, insights_with_br_len = get_directory_insight_len(
                    directory,
                    task_params,
                    project_execution,
                    breakdowns
                )

                print(task_params["log_text"](
                    insights_len=insights_len,
                    nsights_with_br_len=insights_with_br_len)
                )

                if output_file is not None:

                    data_to_json = task_params["log_text"](
                        insights_len=insights_len,
                        insights_with_br_len=insights_with_br_len
                    )

                    for param in data_to_json.split("\n"):

                        param = "{'" + param.replace(":", "': '").\
                            replace(" ", "") + "'}"
                        output_file_current_data.update(eval(param))

            if output_file is not None:
                output_file_data.append(output_file_current_data)

    if output_file is not None:
        json.dump(output_file_data, open(output_file, mode="w"))


if __name__ == "__main__":

    main()

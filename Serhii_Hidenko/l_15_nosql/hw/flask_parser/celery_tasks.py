import json
from celery import Celery


app = Celery("celery_tasks",
             backend='amqp://',
             broker='pyamqp://guest@localhost//')


@app.task
def parse_json(file_content):
    """
    Calculate len of insights
    :param file_content: Insight json
    :type file_content: str
    :return: Tuple of length's
    :rtype: tuple
    """

    insights_len = insights_with_br_len = 0
    breakdowns = [
        "dimension:operating_system",
        "dimension:make",
        "dimension:model",
        "dimension:age",
        "dimension:gender",
        "dimension:interest_category_name",
        "dimension:interest_category_id",
        "dimension:country",
        "dimension:region"
    ]

    for insight in json.loads(file_content):

        if "dimensions" not in insight:
            return insights_len, insights_with_br_len

        insights_len += 1

        dimensions = insight["dimensions"]

        if isinstance(dimensions, str):
            dimensions = json.loads(dimensions.replace("'", '"'))

        insights_with_br_len += int(
            any(
                filter(
                    lambda dimension:
                    dimension["name"] in breakdowns,
                    dimensions,
                )
            )
        )

    return insights_len, insights_with_br_len

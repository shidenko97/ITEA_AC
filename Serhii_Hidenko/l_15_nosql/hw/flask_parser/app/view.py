from flask import redirect, render_template, request, url_for
from app import app
from app.forms import FileForm
from celery_tasks import parse_json


@app.route('/', methods=['POST', 'GET'])
def parse_file():
    """Form action"""

    if request.method == 'POST':
        file = request.files['file']
        celery_task = parse_json.delay(file.read().decode())
        task_id = celery_task.task_id

        return redirect(url_for('get_parse_status', task_id=task_id))

    form = FileForm()
    return render_template('form.html', form=form)


@app.route('/status/<task_id>', methods=['GET'])
def get_parse_status(task_id):
    """Action with task status"""

    task = parse_json.AsyncResult(task_id)

    if task.ready():
        result = task.result
        task_info = {
            "Status": "Completed",
            "Insights len": result[0],
            "Insights with br len": result[1]
        }
    else:
        task_info = {
            "Status": "Pending"
        }

    return render_template('status.html', task_id=task_id, task_info=task_info)

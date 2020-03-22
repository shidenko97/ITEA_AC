from celery import Celery

app = Celery("celery_examples_tasks", backend='rpc://')


@app.task
def sentence_length(sentence):
    return len(sentence)


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


# celery -A tasks worker --loglevel=info

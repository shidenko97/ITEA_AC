from celery_examples_tasks import sentence_length, add, xsum, mul

result = sentence_length.delay("my sentence")
result.ready()
result.get()
result = add.delay(1, 2)
result.ready()
result.get()
result.get(propagate=False)
result = mul.delay(1, 2)
result = xsum.delay(1)

import cProfile


cProfile.run(
    "sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))"
)

cProfile.run(
    "sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])"
)

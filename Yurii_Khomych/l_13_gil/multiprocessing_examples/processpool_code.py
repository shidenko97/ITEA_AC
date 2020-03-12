import time
from concurrent.futures import ProcessPoolExecutor


def basic_func(x):
    if x == 0:
        return "zero"
    elif x % 2 == 0:
        return "even"
    else:
        return "odd"


def multiprocessing_func(x):
    y = x * x
    time.sleep(2)
    print(
        "{} squared final_results in a/an {} number".format(x, basic_func(y))
    )


if __name__ == "__main__":
    starttime = time.time()
    ex = ProcessPoolExecutor(max_workers=10)
    results = ex.map(multiprocessing_func, range(0, 10))
    real_results = list(results)
    print("That took {} seconds".format(time.time() - starttime))

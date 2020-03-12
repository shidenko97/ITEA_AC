import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread


def basic_func(x):
    if x == 0:
        return "zero"
    elif x % 2 == 0:
        return "even"
    else:
        return "odd"


def multitreading_func(x):
    y = x * x
    time.sleep(2)
    result = basic_func(y)
    print(
        "{} squared final_results in a/an {} number".format(x, result)
    )
    return result


if __name__ == "__main__":
    starttime = time.time()
    ex = ThreadPoolExecutor(max_workers=10)
    results = ex.map(multitreading_func, range(0, 10))
    real_results = list(results)
    print("That took {} seconds".format(time.time() - starttime))

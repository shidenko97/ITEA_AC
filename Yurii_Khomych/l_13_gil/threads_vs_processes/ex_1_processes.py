import multiprocessing
import random
import time
from functools import reduce


def func(number):
    random_list = random.sample(range(100000), number)
    return reduce(lambda x, y: x * y, random_list)


if __name__ == "__main__":
    starttime = time.time()
    number = 50000
    process1 = multiprocessing.Process(target=func, args=(number,))
    process2 = multiprocessing.Process(target=func, args=(number,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("That took {} seconds".format(time.time() - starttime))

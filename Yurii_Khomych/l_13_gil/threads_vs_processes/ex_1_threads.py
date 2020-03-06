import threading
import random
import time
from functools import reduce


def func(number):
    random_list = random.sample(range(100000), number)
    return reduce(lambda x, y: x * y, random_list)


if __name__ == "__main__":
    starttime = time.time()
    number = 50000
    thread1 = threading.Thread(target=func, args=(number,))
    thread2 = threading.Thread(target=func, args=(number,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("That took {} seconds".format(time.time() - starttime))

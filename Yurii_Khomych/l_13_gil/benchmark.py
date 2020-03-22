import time
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def cpu_heavy(n):
    count = 0
    for i in range(n):
        count += i
    return count


if __name__ == '__main__':
    starttime = time.time()
    ex = ThreadPoolExecutor(max_workers=10)
    # ex = ProcessPoolExecutor(max_workers=10)
    results = ex.submit(cpu_heavy, 1000000000)
    # cpu_heavy(100000000)
    results.result()
    print("That took {} seconds".format(time.time() - starttime))


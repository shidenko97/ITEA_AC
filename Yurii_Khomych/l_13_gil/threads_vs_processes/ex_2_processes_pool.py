import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor

import requests
import time


def func():
    url = "https://docs.python.org/3/library/concurrent.futures.html"
    response = requests.get(url)
    with open("processes_example.com.txt", "w") as output:
        output.write(response.text)


if __name__ == "__main__":
    starttime = time.time()
    number = 50
    ex = ProcessPoolExecutor(max_workers=50)
    results = [ex.submit(func) for i in range(number)]
    real_results = [res.result() for res in results]

    print("That took {} seconds".format(time.time() - starttime))

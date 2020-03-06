import requests
import time
from concurrent.futures.thread import ThreadPoolExecutor


def func():
    url = "https://docs.python.org/3/library/concurrent.futures.html"
    response = requests.get(url)
    with open("threads_example.com.txt", "w") as output:
        output.write(response.text)


if __name__ == "__main__":
    starttime = time.time()
    number = 50
    ex = ThreadPoolExecutor(max_workers=50)
    results = [ex.submit(func) for i in range(number)]
    real_results = [res.result() for res in results]
    print("That took {} seconds".format(time.time() - starttime))

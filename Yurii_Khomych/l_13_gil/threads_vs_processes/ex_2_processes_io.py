import multiprocessing
import requests
import time


def func(number):
    url = "https://docs.python.org/3/library/concurrent.futures.html"
    for i in range(number):
        response = requests.get(url)
        with open("processes_example.com.txt", "w") as output:
            output.write(response.text)


if __name__ == "__main__":
    starttime = time.time()
    number = 50
    process1 = multiprocessing.Process(target=func, args=(number,))
    process2 = multiprocessing.Process(target=func, args=(number,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("That took {} seconds".format(time.time() - starttime))

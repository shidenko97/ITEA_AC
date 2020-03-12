import requests
import threading
import time


def func(number):
    url = "https://docs.python.org/3/library/concurrent.futures.html"
    for i in range(number):
        response = requests.get(url)
        with open("threads_example.com.txt", "w") as output:
            output.write(response.text)


if __name__ == "__main__":
    starttime = time.time()
    number = 50
    thread1 = threading.Thread(target=func, args=(number,))
    thread2 = threading.Thread(target=func, args=(number,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("That took {} seconds".format(time.time() - starttime))

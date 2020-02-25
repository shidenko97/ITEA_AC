import sys
from contextlib import contextmanager


class MyContextManager:
    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit")


@contextmanager
def my_context_manager():
    print("enter")
    yield
    print("exit")


with MyContextManager():  # enter
    print("do")  # do
# exit


with my_context_manager():  # enter
    print("do")  # do
# exit

#
# from contextlib import suppress
#
# with suppress(FileNotFoundError):
#     with open('fauxfile.txt') as fobj:
#         for line in fobj:
#             print(line)


with open("text.txt", "w") as fobj:
    sys.stdout = fobj
    help(sum)

from contextlib import redirect_stdout, redirect_stderr

with open("text.txt", "w") as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)

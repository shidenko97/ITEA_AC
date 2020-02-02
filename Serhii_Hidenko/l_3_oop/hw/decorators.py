import functools
import time


def execution_time_and_result_decorator(func=None, *, filename="functions_executions.txt"):
    """Decorator for writing to file functions execution time and results"""

    def outer_wrapper(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            time_start = time.time()
            func_return = func(*args, **kwargs)
            runtime = time.time() - time_start

            with open(filename, "a") as file:
                file.write(f"function {func.__name__}\n\texecution time: {runtime} seconds\n\tresult: {func_return}\n")

            return func_return

        return wrapper

    return outer_wrapper
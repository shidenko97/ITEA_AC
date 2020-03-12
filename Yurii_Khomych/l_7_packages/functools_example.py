import functools


def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@functools.total_ordering
class Student:
    def _is_valid_operand(self, other):
        return hasattr(other, "lastname") and hasattr(other, "firstname")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.lastname.lower(), self.firstname.lower()) == (
            other.lastname.lower(),
            other.firstname.lower(),
        )

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.lastname.lower(), self.firstname.lower()) < (
            other.lastname.lower(),
            other.firstname.lower(),
        )

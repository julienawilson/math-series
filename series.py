"""This code houses the fibonacci and lucas functions."""


def fibonacci(n):
    """Return the nth number in the fibonaci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    return 0

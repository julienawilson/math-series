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
    """Return the nth number in the lucas series."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """Determine nth number in series with starting values of a and b."""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n - 1) + sum_series(n - 2)

"""Tests for series function."""
import pytest


FIBONACCI_NUMBERS = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 5],
    [6, 8],
    [7, 13],
    [8, 21],
    [9, 34],
    [10, 55],
]

@pytest.mark.parametrize("n, result", FIBONACCI_NUMBERS)
def test_fibonacci(n, result):
    """test fibonacci for some value of n."""
    from series import fibonacci
    assert fibonacci(n) == result


def test_fibonacci_exists():
    """Test whether fibonacci function exists."""
    import series
    assert series.fibonacci


def test_fib_0():
    """Test output of fibanacci with argument 0."""
    from series import fibonacci
    assert fibonacci(0) == 0

"""Tests for series function."""
import pytest


FIBONACCI_NUMBERS = [
    [0, 0],
    [1, 1],
]

@pytest.mark.parametrize("n, result", FIBONACCI_NUMBERS)
def test_fibonacci(n, result):
    """test fibonacci for some value of n."""
    import series
    assert series.fibonacci(n) == result
    

def test_fibonacci_exists():
    """Test whether fibonacci function exists."""
    import series
    assert series.fibonacci


def test_fib_0():
    """Test output of fibanacci with argument 0."""
    from series import fibonacci
    assert fibonacci(0) == 0

"""Tests for series function."""


def test_fibonacci_exists():
    """Test whether fibonacci function exists."""
    import series
    assert series.fibonacci


def test_fib_0():
    """Test output of fibanacci with argument 0."""
    from series import fibonacci
    assert fibonacci(0) == 0

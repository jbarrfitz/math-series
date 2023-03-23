from series import fibonacci, lucas


def test_fibonacci_exists():
    assert fibonacci


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_ten():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_fibonacci_negative():
    actual = fibonacci(-4)
    expected = 0
    assert actual == expected


def test_fibonacci_non_numeric():
    actual = fibonacci("Feel the love!")
    expected = 0
    assert actual == expected


def test_lucas_exists():
    assert lucas
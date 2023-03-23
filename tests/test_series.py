from series import fibonacci, lucas, sum_series


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


def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_seven():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_lucas_negative():
    actual = lucas(-234)
    expected = 0
    assert actual == expected


def test_lucas_decimal():
    actual = lucas(4.43)
    expected = 0
    assert actual == expected


def test_lucas_non_number():
    actual = lucas("Some random text")
    expected = 0
    assert actual == expected


def test_sum_series_exists():
    assert sum_series


def test_sum_series_zero_one_two():
    actual = sum_series(0, 1, 2)
    expected = 1
    assert actual == expected



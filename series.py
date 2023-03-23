def fibonacci(n):
    """
    Calculates the nth position of the fibonacci sequence
    :param n: the position within the fibonacci sequence being calculated (zero-indexed)
    :return: integer at the nth position of the fibonacci sequence, or zero (0) if
    argument provided is invalid.
    """

    if type(n) != int or n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """
    Calculates the nth position of the lucas sequence
    :param n: the position within the lucas sequence being calculated (zero-indexed)
    :return: integer at the nth position of the lucas sequence, or zero (0) if
    argument provided is invalid.
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    if type(n) != int or n < 0:
        return 0
    return lucas(n - 2) + lucas(n - 1)


def sum_series(n, first_num=0, second_num=1):
    """
    Calculates the nth position of a fibonacci-like sequence whose first two digits
    are first_num and second_num.
    :param n: the position within the sequence to be calculated (zero-indexed)
    :param first_num: the first number (position 0) of the sequence. Zero (0) if omitted.
    :param second_num: the second number (position 1) of the sequence. One (1) if omitted.
    :return: integer at the nth position of the sequence, or zero (0) if invalid argument(s)
    are provided.
    """
    if n == 0:
        return first_num
    if n == 1:
        return second_num
    return sum_series(n - 2, first_num, second_num) + sum_series(n - 1, first_num, second_num)


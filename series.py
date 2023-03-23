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
    return lucas(n - 2) + lucas(n - 1)
"""Test personal pyment.

This is a test.
"""


def addnum_npy(a: int, b: int = 0) -> int:
    """Add numbers.

    Args:
        a (int): First number.
        b (int, optional): Second number. By default, 0.

    Returns:
        int: The output sum.
    >>> addnum_npy(0, 1)
    1
    """
    return a + b


def addnum_rest(a: int, b: int = 0) -> int:
    """Add numbers.

    Args:
        a (int): First number.
        b (int, optional): Second number. By default, 0.

    Returns:
        int: The output sum.
    """
    return a + b


def addnum_google(a: int, b: int = 0) -> int:
    """Add numbers.

    Args:
        a (int): first number.
        b (int, optional): second number. By default, 0.

    Returns:
        int: Int: The output sum.
    """
    return a + b


def addnum_partialdoc(a: int, b: int = 0) -> int:
    """Add numbers.

    Args:
        a (int): first number.
        b (int, optional): By default, 0.
    """
    return a + b


def addnum_onlytitle(a: int, b: int = 0) -> int:
    """Add numbers."""
    return a + b


def addnum_moredesc(a: int, b: int = 0) -> int:
    """Add number.

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
    Eiusmod tempor incididunt ut labore et dolore magna aliqua.
    """
    return a + b


def addnum_nothing(a, b=0):
    """"""
    return a + b


def addnum_complex(a: int, b: int = 0) -> int:
    """Add numbers.

    Args:
        a (int): First number.
    It is an int.
        b (int, optional): Second number. By default, 0.

    Returns:
        int: The output sum.

    Notes
    -----
        This function also works for negative numbers.

    Examples
    --------
        >>> addnum_complex(0, 1)
        1
    """
    return a + b

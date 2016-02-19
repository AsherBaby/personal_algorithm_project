"""
Next r-combination
"""

def next_r_combination(n, c1):
    # type: (int, str) -> list
    """
    >>> next_r_combination(6, '[1,2,5,6]')
    [1, 3, 4, 5]
    """
    r = len(c1)
    i = r - 1
    while i >= 0:
        if c1[i] != n - r + i + 1:
            # if ith element is not of last possible
            break
        i -= 1

    c1[i] += 1
    i += 1
    while i < r:
        c1[i] = c1[i-1] + 1
        i += 1
    return c1

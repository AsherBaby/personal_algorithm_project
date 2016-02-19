"""
Compute next permutation of P1 without duplicates

Run doctest: python -m doctest -v next_permutation.py
"""

def next_permutation(p1):
    # type: (list) -> list
    """
    >>> next_permutation([2, 3, 4, 1, 6, 5])
    [2, 3, 4, 5, 1, 6]
    """
    n = len(p1)
    i = n - 2
    while i >= 0:
        if p1[i] < p1[i+1]:
            break
        i -= 1

    j = n - 1
    while j > i:
        if p1[j] > p1[i]:
            break
        i -= 1

    p1[i], p1[j] = p1[j], p1[i]

    p1[i+1:] = reversed(p1[i+1:])
    return p1

"""
Max non-overlapping intervals problem, also AKA activity selection
problem.

Greedy algorithm.
"""

class Interval:
    def __init__(self, s, f):
        self.s = s
        self.f = f

def max_non_overlapping_intervals(a):
    # type: (list) -> int
    """
    >>> a = [Interval(0,1), Interval(2,4), Interval(1,3)]
    >>> max_non_overlapping_intervals(a)
    2
    """
    a.sort(key=lambda x: x.f)
    n = len(a)
    count = 0
    f = 0
    for interval in a:
        if interval.s >= f:
            count += 1
            f = interval.f
    return count

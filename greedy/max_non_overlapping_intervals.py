"""
Max non-overlapping intervals problem, also AKA activity selection
problem.

Greedy algorithm.
"""

class Interval:
    def __init__(self, s, f):
        self.s = s
        self.f = f

def max_non_overlapping_intervals(A):
    A.sort(key=lambda x: x.f)
    count = 0
    f = 0
    for interval in A:
        if f <= interval.s:
            count += 1
            f = interval.f
    return count

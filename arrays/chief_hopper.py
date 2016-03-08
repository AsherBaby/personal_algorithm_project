"""
Chief Hopper Problem

This piece of code is unprecedented for the self-defined
sequence class and the compute-when-need array.
"""
from bisect import bisect_left
import collections
from pprint import pprint as print

A = [int(x) for x in input().strip().split()]

class FinalEnergyList(collections.Sequence):

    def __init__(self, f, n):
        self.f = f
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, x):
        if not (0 <= x < self.n):
            raise IndexError
        return self.f(x)

def f(x):
    for h in A:
        x = 2*x - h
    return x

ans = bisect_left(FinalEnergyList(f, pow(10, 5)), 0)
print(ans)

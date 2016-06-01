"""
Given 2*n + 2 numbers, every numbers occurs twice except two, find them.
"""


from collections import Counter

def singleNumberIII(A):
    return map(lambda x: x[0], Counter(A).most_common()[-2:])

if set(singleNumberIII([1,2,3,3,2,4,1,5])) != {4, 5}:
    raise AssertionError
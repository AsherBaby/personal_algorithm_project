"""
Problem:
Given a bitstream, flip a segment of it to make the bitstream have
maximum number of 1s.

Solution:
Convert 0 to -1. Transform the problem to minimum subarray sum problem.
"""

def flip_bits(s):
    """
    O(n) algorithm
    s: a string of 0s or 1s
    return: maximum number of 1s after flip
    """
    a = [int(c) for c in s]
    n = len(a)
    for i in range(n):
        if a[i] == 0:
            a[i] = -1
    local_min = [float('inf')] * n
    local_min[0] = a[0]
    left_index = list(range(n))
    global_min = a[0]
    global_min_index = 0
    for i in range(1, n):
        if local_min[i-1] < 0:
            local_min[i] = a[i] + local_min[i-1]
            left_index[i] = left_index[i-1]
        else:
            local_min[i] = a[i]
        if local_min[i] < global_min:
            global_min = local_min[i]
            global_min_index = i
    left = left_index[global_min_index]
    right = global_min_index
    for i in range(left, right+1):
        if a[i] == -1:
            a[i] = 1
        else:
            a[i] = -1
    return a.count(1)

def  flip_bits2(s):
    """
    O(n^2) algorithm
    """
    b = [int(c) for c in s]
    n = len(b)
    ones = [0] * (n+1)  # num of ones before index i
    for i in range(n):
        ones[i+1] = ones[i] + b[i]
    max_gain = 0
    for l in range(n):
        for r in range(l, n):
            total_ones = ones[r+1] - ones[l]
            total = r + 1 - l
            total_zeros = total - total_ones
            gain = total_zeros - total_ones
            max_gain = max(max_gain, gain)
    return max_gain + ones[n]

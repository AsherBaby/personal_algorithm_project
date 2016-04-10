"""
Quick select, O(n)
"""
#import ipdb; ipdb.set_trace()
import random

def quick_select(A, k):
    return _quick_select(A, 0, len(A)-1, k)

def _quick_select(A, l, r, k):
    pivot = _partition(A, l, r, random.randint(l, r))
    if pivot == k:
        return A[pivot]
    elif k < pivot:
        return _quick_select(A, l, pivot-1, k)
    else:
        return _quick_select(A, pivot+1, r, k)

def _partition(A, l, r, pivot):
    A[l], A[pivot] = A[pivot], A[l]
    target = A[l]
    i = l+1
    for j in range(l+1, r+1):
        if A[j] < target:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    return i-1

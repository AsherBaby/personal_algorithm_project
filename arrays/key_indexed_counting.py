"""
This is a specific key indexed counting for ASCII alphabet.

However, key indexed counting is useful in a more general purpose. It
can sort keys with small range.

For example, sort a million of transactions with timestamps in a day.
Analysis:
    There are 86,400 kinds of timestamps in a day, which we refer to R.
The key indexed counting sort timestamps in O(N + R), while quick-sort
takes O(N lgN).
"""

def key_indexed_counting(a, key=lambda x: x):
    count = [0] * 129
    for item in a:
        count[ord(key(item))+1] += 1

    for i in range(128):
        count[i+1] += count[i]

    aux = [None] * len(a)
    for item in a:
        aux[count[ord(key(item))]] = item
        count[ord(key(item))] += 1

    for i in range(len(a)):
        a[i] = aux[i]

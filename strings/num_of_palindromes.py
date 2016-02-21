"""
An O(n^2) algorithm without using extra space to compute the
number of palindromes in a string.
"""

def num_of_palindromes(s):
    n = len(s)
    count = 0
    for i in range(n):
        w = 0  # width
        while 0 <= i-w and i+w < n and s[i-w] == s[i+w]:
            count += 1
            w += 1
        w = 0
        while 0 <= i-w and i+w+1 < n and s[i-w] == s[i+w+1]:
            count += 1
            w += 1
    return count

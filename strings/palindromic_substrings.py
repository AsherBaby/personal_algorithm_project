"""
O(n^2) algorithm without extra space.
"""

def palindromic_substrings(s):
    """
    >>> palindromic_substrings('aba')
    4
    >>> palindromic_substrings('abba')
    6
    """
    count = 0
    i = 0
    n = len(s)
    for i in range(n):
        w = 0
        while 0 <= i-w and i+w < n:
            if s[i-w] == s[i+w]:
                count += 1
                w += 1
            else:
                break
        w = 0
        while 0 <= i-w and i+w+1 < n:
            if s[i-w] == s[i+w+1]:
                count += 1
                w += 1
            else:
                break
    return count

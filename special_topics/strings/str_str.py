"""
An O(n^2) algorithm
"""

def search(s, p):
    # search p[attern] in s[tring]
    for i in range(len(s)):
        mismatch = False
        for j in range(len(p)):
            if i+j >= len(s) or s[i+j] != p[j]:
                mismatch = True
                break
        if not mismatch:
            return i
    return -1

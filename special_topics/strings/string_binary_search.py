"""
Binary search in a sorted list of strings is typically the same with
binary search for numbers. However, the various lengths of strings can
make code a little bit tricky.
The code below works in the scenario when need to find strings having
the prefix that being provided.

Note: a sorted list is not a prime choice of container for strings.
Trie can have better space efficiency and add/delete support over
sorted list.
"""

def string_binary_search(A, prefix):
    # type: (list, string) -> list
    """
    >>> A = ['apple', 'avocado', 'banana', 'coconut']
    >>> string_binary_search(A, 'av')
    ['avocado']
    >>> string_binary_search(A, 'ax')
    >>> string_binary_search(A, 'bananana')
    """
    first = 0
    last = len(A) - 1
    for i, c in enumerate(prefix):
        l = first
        r = last
        while l < r:
            m = (l + r) // 2
            if i >= len(A[m]) or A[m][i] < c:
                l = m + 1
            else:
                r = m
        if i >= len(A[l]) or A[l][i] != c:
            """
            A[l] is supposed to be the first match
            if prefix is too long or does not match, it means no match
            exists in the string list.
            """
            return
        first = l
        r = last
        while l < r:
            m = (l + r + 1) // 2
            if A[m][i] <= c:
                l = m
            else:
                r = m - 1
        last = l
    return A[first:last+1]

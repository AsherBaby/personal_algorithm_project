
import math

def permutation_index(s):
    # type: (str) -> int
    """
    >>> permutation_index('1423')
    4
    >>> permutation_index('3412')
    16
    """
    n = len(s)
    # P(n)
    radix = math.factorial(n-1)
    index = 0
    for i in range(n-1):
        count = 0
        for j in range(i, n):
            if s[j] < s[i]:
                count += 1
        index += radix * count
        radix //= n - 1 - i
    return index

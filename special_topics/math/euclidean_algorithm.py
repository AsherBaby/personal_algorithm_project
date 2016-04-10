"""
Euclidean algorithm of greatest common divisor
(iterative version)
"""

def gcd(a, b):
    # a = qb + r -> gcd(a, b) = gcd(b, r)
    """
    >>> gcd(414, 662)
    2
    """
    x = max(a, b)
    y = min(a, b)
    while y:
        x, y = y, x%y
    return x

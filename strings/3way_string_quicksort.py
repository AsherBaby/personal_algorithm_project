"""
Three-way string quicksort, is the mothod of choice for sorting string
in general cases.
"""

def string_sort(a):
    # type: (list) -> None
    """
    Main function
    >>> a = ['apple', 'pear', 'applejuice', 'orange', 'orange']
    >>> string_sort(a)
    >>> a
    ['apple', 'applejuice', 'orange', 'orange', 'pear']
    """
    _sort(a, 0, len(a)-1, 0)

def _sort(a, l, r, k):
    # type: (list, int, int, int) -> None
    """
    Recursive function.
    l: left bound
    r: right bound
    k: kth index of one string
    """
    if l >= r:  # if list is empty or contains only one string
        return
    lt, gt = _three_way_partition(a, l, r, k)

    _sort(a, l, lt-1, k)
    if char_at(a[lt], k) != chr(0):
        _sort(a, lt, gt, k+1)
    _sort(a, gt+1, r, k)

def _three_way_partition(a, l, r, k):
    lt = l
    gt = r
    i = l + 1
    t = char_at(a[lt], k)
    while i <= gt:
        if char_at(a[i], k) < t:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif char_at(a[i], k) > t:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def char_at(s, k):
    return s[k] if k < len(s) else chr(0)

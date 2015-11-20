
"""
Inversion count of two arrays, implemented with Divide and Conquer.
Time Complexicity: O(n log(n))
Usage: Inversion count can be used for measuring silimarity of two
arrays, for example: two ranking arrays. Therefore inversion count is
kind of the essence in recommendation algorithm.
"""

def inversion_count(array_a, array_b):
    hash_a = {}
    for i, val in enumerate(array_a):
        hash_a[val] = i
    hash_a[float('inf')] = float('inf')
    return _inversion_count(array_b, 0, len(array_b)-1, hash_a)

def cmp(a, b, hash):
    return hash[a] < hash[b]

def _inversion_count(array, l, r, hash):
    if l >= r:
        return 0
    mid = (l + r) // 2
    l_count = _inversion_count(array, l, mid, hash)
    r_count = _inversion_count(array, mid+1, r, hash)
    crossing_count = _crossing_inversion_count(array, l, mid, r, hash)
    return l_count + crossing_count + r_count

def _crossing_inversion_count(array, l, mid, r, hash):
    l_array = array[l : mid+1]
    l_array.append(float('inf'))
    r_array = array[mid+1 : r+1]
    r_array.append(float('inf'))
    i = 0
    j = 0
    n = mid - l + 1
    count = 0
    for k in range(l, r):
        if cmp(l_array[i], r_array[j], hash):
            array[k] = l_array[i]
            i += 1
        else:
            array[k] = r_array[j]
            j += 1
            count += n - i
    return count

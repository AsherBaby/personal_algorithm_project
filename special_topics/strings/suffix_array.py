"""
Linearithmic algorithm for building suffix array.
"""
#import ipdb; ipdb.set_trace()

class SuffixArray:
    """
    Test case from 'http://www.allisons.org/ll/AlgDS/Strings/Suffix/'
    >>> suffix_array = SuffixArray('mississippi')
    >>> suffix_array.suffix
    [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
    """

    def __init__(self, s):
        self.s = s
        self.suffix = None
        self.inverse = None
        self._build_suffix_array()  # generate suffix and inverse array

    def _build_suffix_array(self):
        s = self.s
        n = len(s)
        suffix = list(range(n))
        inverse = list(range(n))
        flag = [False] * n  # check if row is sorted
        suffix.sort(key=lambda x: s[x])
        for i, v in enumerate(suffix):
            inverse[v] = i
        k = 2
        while k < n:
            l = 0
            m = k // 2 - 1  # index of last sorted char
            while l < n:
                if flag[l]:
                    l += 1
                    continue
                r = l + 1
                while r < n and suffix[l]+m<n and suffix[r]+m<n and s[suffix[l]+m]==s[suffix[r]+m]:
                    r += 1
                if r - l == 1:
                    flag[l] = True
                    l += 1
                else:
                    suffix[l:r] = sorted(suffix[l:r], key=lambda x: inverse[x+k//2] if x+k//2<n else -1)
                    l = r
            for i, v in enumerate(suffix):
                inverse[v] = i
            k *= 2
        self.suffix = suffix
        self.inverse = inverse

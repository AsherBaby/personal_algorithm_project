

class Solution:

    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, (n+1)//2)
        else:
            smaller = self.findKth(A, B, n//2)
            bigger = self.findKth(A, B, n//2+1)
            return (smaller + bigger) / 2.0


    def findKth(self, A, B, k):
        # k starts with 1
        if not A:
            return B[k-1]
        if not B:
            return A[k-1]
        if k == 1:
            return min(A[0], B[0])

        a = A[k//2-1] if k//2 <= len(A) else None
        b = B[k//2-1] if k//2 <= len(B) else None

        if a is None:
            return self.findKth(A, B[k//2:], k-k//2)
        if b is None or a < b:
            return self.findKth(A[k//2:], B, k-k//2)
        else:
            return self.findKth(A, B[k//2:], k-k//2)
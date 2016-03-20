"""
6 5 2
7 5 4
9 2 6

ans: 9 -> 5 -> 6 : 5
"""

def max_min_path(A):
    m = len(A)
    n = len(A[0])
    if m == 1:
        return min(A)
    for y in range(1, n):
        for x in range(m):
            if x == 0:
                A[x][y] = min(A[x][y], max(A[x][y-1], A[x+1][y-1]))
            elif 0 < x < m-1:
                A[x][y] = min(A[x][y], max(A[x][y-1], A[x-1][y-1], A[x+1][y-1]))
            else:
                A[x][y] = min(A[x][y], max(A[x][y-1], A[x-1][y-1]))
    return max(row[-1] for row in A)  # loving it!

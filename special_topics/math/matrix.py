"""
Matrix implementation and its arithmetics
"""

class Matrix:
    """
    >>> m1 = Matrix(2, 2, [1,2,3,4])
    >>> m2 = Matrix(2, 2, [4,3,2,1])
    >>> m1.product(m2)
    >>> m1.data
    [[8, 5], [20, 13]]
    """

    def __init__(self, m, n, array):
        self.m = m
        self.n = n
        self.data = [[0]*n for i in range(m)]
        self._build(array)

    def _build(self, array):
        k = 0
        for i in range(self.m):
            for j in range(self.n):
                self.data[i][j] = array[k]
                k += 1

    def product(self, m2):
        data = [[0]*m2.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(m2.n):
                cij = 0
                for k in range(self.n):
                    cij += self.data[i][k] * m2.data[k][j]
                data[i][j] = cij
        self.data = data

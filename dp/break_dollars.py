"""
Given set A, and target t, find the number of different
combinations of elements in A (allow use unlimited times) that sum
to t.
"""

class BreakDollars:

    def __init__(self, A, t):
        self.A = A
        self.n = len(A)
        self.t = t
        self.ans = 0

    def solve(self):

        dp = [[0] * (self.t+1) for _ in range(self.n+1)]
        dp[0][0] = 1
        for i in range(1, self.n+1):
            for j in range(self.t+1):
                dp[i][j] += dp[i-1][j]
                k = j - self.A[i-1]
                while k >= 0:
                    dp[i][j] += dp[i-1][k]
                    k -= self.A[i-1]

        return dp[self.n][self.t]

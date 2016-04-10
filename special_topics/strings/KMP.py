"""
KMP substring search algorithm
"""

class KMP:

    def __init__(self, pattern):
        self.dp = None
        self.preprocessing(pattern)
        self.pattern = pattern

    def search(self, text):
        i = 0
        j = 0
        while i < len(text) and j < len(self.pattern):
            j = self.dp[ord(text[i])][j]
            i += 1
        if j == len(self.pattern):
            return i - j
        else:
            return -1

    def preprocessing(self, pattern):
        self.dp = [[0] * len(pattern) for j in range(256)]
        dp = self.dp
        dp[ord(pattern[0])][0] = 1
        x = 0
        for j in range(1, len(pattern)):
            for i in range(256):
                dp[i][j] = dp[i][x]  # mismatch
            dp[ord(pattern[j])][j] = j + 1  # match
            x = dp[ord(pattern[j])][x]  # update x

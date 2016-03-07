"""
3 5 3
2 3 4
1 0 1

5-3-2-1-0 longest skiing path
"""


class LongestSkiiingPath:

    def longest_skiing_path(self, grid):
        self.grid = grid
        self.dp = [[0] * len(grid) for i in range(len(grid[0]))]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                self.dfs(x, y)
        return max(map(max, matrix))

    def dfs(self, x, y):
        if self.dp[x][y] > 0:
            return self.dp[x][y]
        for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
            nx = dx + x
            ny = dy + y
            if (0<=nx and nx<len(self.grid) and
                    0<=ny and ny<len(self.grid[0]) and
                    self.grid[nx][ny] < self.grid[x][y]):
                self.dp[x][y] = max(self.dp[x][y], 1+self.dfs(nx, ny))
        return self.dp[x][y]

grid = [
    [3, 5, 3],
    [2, 3, 4],
    [1, 0, 1],
]
ans = LongestSkiiingPath().longest_skiing_path(grid)
print(ans)

"""
Sudoku solver
"""
class Sudoku:

    def solve(self, grid):
        self.grid = grid
        if self.dfs(0, 0):
            return self.grid

    def dfs(self, i, j):
        if i == 9:
            return True
        if self.grid[i][j]:
            if self.valid(i, j) and self.dfs(*self.next(i, j)):
                return True
            return False
        for x in range(1, 10):
            self.grid[i][j] = x  # try
            if self.valid(i, j) and self.dfs(*self.next(i, j)):
                return True
        self.grid[i][j] = 0  # reset
        return False

    def valid(self, i, j):
        x = self.grid[i][j]
        return (
            self.grid[i].count(x) < 2 and
            [row[j] for row in self.grid].count(x) < 2 and
            self.square(i, j).count(x) < 2)

    def square(self, i, j):
        i //= 3
        j //= 3
        ret = []
        for x in range(i*3, i*3+3):
            for y in range(j*3, j*3+3):
                if self.grid[x][y]:
                    ret.append(self.grid[x][y])
        return ret

    def next(self, i, j):
        return (i, j+1) if j < 8 else (i+1, 0)

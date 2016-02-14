"""
Sudoku solver
"""
#import ipdb; ipdb.set_trace()
class Sudoku:

    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        return self.dfs(0, 0)

    def dfs(self, i, j):
        if self.is_last(i, j):
            return True

        grid = self.grid
        if grid[i][j]:
            #!! pre-filled
            if self.valid(i, j):
                n_i, n_j = self.next(i, j)
                if self.dfs(n_i, n_j):
                    return True
            return False

        for x in range(1, 10):
            grid[i][j] = x
            if self.valid(i, j):
                n_i, n_j = self.next(i, j)
                if self.dfs(n_i, n_j):
                    return True
        #!!
        grid[i][j] = 0
        return False

    def valid(self, i, j):
        x = self.grid[i][j]
        #!!
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

    def is_last(self, i, j):
        return i == 9 and j == 0

    def next(self, i, j):
        return (i, j+1) if j < 8 else (i+1, 0)

"""
Sudoku solver
"""

class Sudoku:

    def __init__(self, board):
        self.board = board

    def solve(self):
        self.dfs(0, 0)
        return self.board

    def dfs(self, i, j):
        if i == 9 and j == 0:
            return True
        for x in range(1, 10):
            if (x not in self.board[i] and
                x not in [row[j] for row in self.board] and
                x not in self.square(i, j)):
                self.board[i][j] = x
                n_i, n_j = self.next(i, j)
                if self.dfs(n_i, n_j):
                    return True
        self.board[i][j] = None

    def square(self, i, j):
        i /= 3
        j /= 3
        ret = []
        for x in range(i*3, i*3+3):
            for y in range(j*3, j*3+3):
                if self.board[x][y]:
                    ret.append(self.board[x][y])
        return ret

    def next(self, i, j):
        if j < 8:
            return i, j+1
        else:
            return i+1, 0

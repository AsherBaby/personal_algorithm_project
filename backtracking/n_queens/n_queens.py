"""
Get all distinct N-Queen solutions
@param n: The number of queens
@return: All distinct solutions
"""
def solveNQueens(n):
    if not n:
        return []

    solutions = []
    dfs(solutions, [], n)
    return drawBoard(solutions, n)

def dfs(solutions, node, n):
    if len(node) == n:
        solutions.append(node[:])
        return
    for i in range(n):
        if valid(i, node):
            node.append(i)
            dfs(solutions, node, n)
            node.pop()

def drawBoard(solutions, n):
    boards = []
    for s in solutions:
        board = [['.']*n for i in range(n)]
        for col, row in enumerate(s):
            board[row][col] = 'Q'
        board = [''.join(s) for s in board]
        boards.append(board)
    return boards

def valid(queen, queens):
    # check if queen is OK with queens
    if queens.count(queen):
        return False
    queen_row = queen
    queen_col = len(queens)
    for col in range(len(queens)):
        row = queens[col]
        if row + col == queen_row + queen_col:
            return False
        if row - col == queen_row - queen_col:
            return False
    return True

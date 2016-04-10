def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited = set()
            visited.add((i, j))
            if dfs(board, i, j, word, 0, visited):
                return True

    return False

def dfs(board, i, j, word, idx, visited):
    if board[i][j] != word[idx]:
        return False
    if idx == len(word)-1:
        return True
    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]
    for dir in range(4):
        n_i = i + x[dir]
        n_j = j + y[dir]
        if (0 <= n_i and n_i < len(board) and
            0 <= n_j and n_j < len(board[0]) and
            (n_i, n_j) not in visited):
            visited.add((n_i, n_j))
            if dfs(board, n_i, n_j, word, idx+1, visited):
                return True
            visited.remove((n_i, n_j))
    return False

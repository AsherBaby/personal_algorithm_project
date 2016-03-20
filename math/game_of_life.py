def gameOfLife(board):
        """
        encoding:
        0: 0 -> 0
        1: 1 -> 1
        2: 1 -> 0
        3: 0 -> 1
        """
        neighbors = (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
        m = len(board)
        n = len(board[0])
        for x in range(m):
            for y in range(n):
                lives = 0
                for dx, dy in neighbors:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and 1<=board[nx][ny]<=2: # read
                        lives += 1
                if board[x][y]: # write
                    if lives < 2 or lives > 3:
                        board[x][y] = 2
                else:
                    if lives == 3:
                        board[x][y] = 3
        for x in range(m):
            for y in range(n):
                board[x][y] %= 2

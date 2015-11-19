def numIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                islands += 1
                dfs(grid, i, j)

    return islands

def dfs(grid, i, j):
    if grid[i][j] == 0:
        return
    grid[i][j] = 0  # mark visited
    directions = [(0,-1),(-1,0),(0,1),(1,0)]
    for direction in directions:
        new_i, new_j = i+direction[0], j+direction[1]
        if (0 <= new_i and new_i < len(grid) and
            0 <= new_j and new_j < len(grid[0])):
            dfs(grid, new_i, new_j)

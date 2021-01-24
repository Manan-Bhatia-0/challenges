# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally, vertically, or diagonally.
# You may assume all four edges of the grid are all surrounded by water.
#
# Examples:
#
#   Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Cell:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def is_valid_land(i, j, num_row, num_col, grid):
    if (0 <= i < num_row) and (0 <= j < num_col) and (grid[i][j] == "1"):
        return True
    return False


def bfs(r, c, queue, visited, grid, rows, cols):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    queue.append(Cell(r, c))
    visited[r][c] = True
    while queue:
        curr = queue.pop(0)
        for k in range(8):
            x = curr.x + dx[k]
            y = curr.y + dy[k]
            if is_valid_land(x, y, rows, cols, grid) and not visited[x][y]:
                queue.append(Cell(x, y))
                visited[x][y] = True


def num_islands(grid):
    # """
    #    :type grid: List[List[str]]
    #    :rtype: int
    #    """
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    queue = []
    visited = [[False for _ in range(cols)]for _ in range(rows)]  # for some reason this is the inverse
    islands = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and not visited[i][j]:
                bfs(i, j, queue, visited, grid, rows, cols)
                islands += 1
    return islands


def main():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    grid2 = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "1", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    grid3 = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "1", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    grid4 = [
        ["1", "1", "0", "0", "1"],
        ["1", "0", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "1", "0", "1", "1"]
    ]

    isle = num_islands(grid)
    print(f"Number of islands: {isle}")
    isle = num_islands(grid2)
    print(f"Number of islands: {isle}")
    print(f"Number of islands: {num_islands(grid3)}")
    print(f"Number of islands: {num_islands(grid4)}")


if __name__ == "__main__":
    main()


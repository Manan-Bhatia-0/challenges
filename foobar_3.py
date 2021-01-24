# Return the minimum number of moves it takes to move from source
# square to destination square on a chess board when you move like a Knight
class Cell:

    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist


def is_valid(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    return False


def coord(src):
    return int(src / 8), int(src % 8)


def solution(src, dest):

    # Your code here
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = []
    src_pos = (coord(src))
    dest_pos = (coord(dest))
    visited = [[False for i in range(8)]
               for j in range(8)]

    queue.append(Cell(src_pos[0], src_pos[1], 0))
    visited[src_pos[0]][src_pos[1]] = True

    while len(queue) > 0:
        curr = queue[0]
        queue.pop(0)

        if curr.x == dest_pos[0] and curr.y == dest_pos[1]:
            print(queue)
            return curr.dist

        for i in range(8):
            x = curr.x + dx[i]
            y = curr.y + dy[i]

            if is_valid(x, y) and not visited[x][y]:
                visited[x][y] = True
                queue.append(Cell(x, y, curr.dist + 1))


def main():
    moves = solution(6, 31)
    print(moves)


if __name__ == "__main__":
    main()

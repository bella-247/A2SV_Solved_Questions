from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

# sys.setrecursionlimit(200000) # don't forget to use python 3
input = sys.stdin.readline


def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))


def read_int():
    return int(input().strip())


def read_ints():
    return map(int, input().split())


def read_list():
    return list(map(int, input().split()))


def yn(res):
    print("YES" if res else "NO")


inf = float("inf")


# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    n = read_int()

    grid = [list(input().strip()) for _ in range(n)]

    def in_bound(row, col):
        return -1 < row < n and -1 < col < n

    points = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "*":
                points.append([i, j])

    row1, col1 = points[0]
    row2, col2 = points[1]

    if points[0] == points[1]:
        points.extend([points[0]] * 2)

    elif row1 == row2:
        if in_bound(row1 + 1, col1):
            points.append([row1 + 1, col1])
            points.append([row2 + 1, col2])

        elif in_bound(row1 - 1, col1):
            points.append([row1 - 1, col1])
            points.append([row2 - 1, col2])

    elif col1 == col2:
        if in_bound(row1, col1 + 1):
            points.append([row1, col1 + 1])
            points.append([row2, col2 + 1])

        elif in_bound(row1, col1 - 1):
            points.append([row1, col1 - 1])
            points.append([row2, col2 - 1])
    else:
        points.append([row1, col2])
        points.append([row2, col1])

    for row, col in points:
        grid[row][col] = "*"

    for row in grid:
        print("".join(row))


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

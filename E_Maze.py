import random, math, sys, heapq as heap
from itertools import accumulate
from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from random import randint

input = sys.stdin.readline


def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))


def rs():
    return input().strip()


def ri():
    return int(rs())


def rls(spliter=" "):
    return list(map(int, rs().split(spliter)))


def yn(res):
    print("Yes" if res else "No")


def acc(arr):
    return list(accumulate(arr))


rand = random.getrandbits(32)


def xor(x):
    return x ^ rand


# sys.setrecursionlimit(200000)  # don't forget to use python 3


def print_grid(grid):
    for row in grid:
        print("".join(row))


def solution(_):
    n, m, k = rls()
    grid = [list(rs()) for _ in range(n)]

    if k == 0:
        return print_grid(grid)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for _ in range(m)] for __ in range(n)]

    def in_bound(row, col):
        return -1 < row < n and -1 < col < m

    start = [0, 0]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                start = [i, j]
                visited[i][j] = True

    countX = [[0 for _ in range(m)] for __ in range(n)]
    possibilities = [[] for _ in range(m) for __ in range(n)]

    print(possibilities)

    # stack = [start]

    # while stack:
    #     row, col = stack.pop()

    #     possibilities = []

    #     for dr, dc in directions:
    #         nr, nc = row + dr, col + dc

    #         if not in_bound(nr, nc):
    #             continue

    #         if grid[nr][nc] == "#":
    #             continue

    #         if visited[nr][nc]:
    #             continue

    #         visited[nr][nc] = True

    #         possibilities.append([nr, nc])

    #     for direction in directions:

    print_grid(grid)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

import random, math, sys, heapq as heap
from itertools import accumulate
from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from random import randint
from heapq import heapify, heappush, heappop

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
    print("YES" if res else "NO")


def acc(arr):
    return list(accumulate(arr))


rand = random.getrandbits(32)


def xor(x):
    return x ^ rand


# sys.setrecursionlimit(200000) # don't forget to use python 3

INF = 10**18


def solution(_):
    n, m = rls()
    grid = [list(rs()) for _ in range(n)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inbound(row, col):
        return -1 < row < n and -1 < col < m

    def dfs(row, col, color):
        grid[row][col] = color

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if not inbound(nr, nc):
                continue

            if grid[nr][nc] == color:
                grid[row][col] = "."
                return False

            if grid[nr][nc] != ".":
                continue

            if grid[nr][nc] == "." and (not dfs(nr, nc, "B" if color == "W" else "W")):
                grid[row][col] = "."
                return False

        return True

    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                if not dfs(i, j, "B"):
                    dfs(i, j, "W")

    for row in grid:
        print("".join(row))


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

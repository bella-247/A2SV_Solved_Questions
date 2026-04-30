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


sys.setrecursionlimit(200000) # don't forget to use python 3


def solution(_):
    n, m = rls()

    grid = [list(rs()) for _ in range(n)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    # 0 1 2
    def in_bound(row, col):
        return -1 < row < n and -1 < col < m

    def dfs(row, col, parent):

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if not in_bound(nr, nc):
                continue

            if grid[row][col] != grid[nr][nc]:
                continue

            if parent and parent == [nr, nc]:
                continue

            if visited[nr][nc] == 2:
                continue

            if visited[nr][nc] == 1:
                return True

            visited[nr][nc] = 1
            
            if dfs(nr, nc, [row, col]):
                return True
            
            visited[nr][nc] = 2

        return False

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                visited[i][j] = 1
                if dfs(i, j, []):
                    return yn(1)
                visited[i][j] = 2

    yn(0)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

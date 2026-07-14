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


def solution(_):
    n, m = rls()

    grid = [rs() for _ in range(n)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * m for _ in range(n)]

    distance = [[-inf] * m for _ in range(n)]

    def inbound(row, col):
        return -1 < row < n and -1 < col < m

    q = deque()

    goal = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "t":
                visited[i][j] = True
                q.append((i, j))

            elif grid[i][j] == "K":
                goal = [i, j]

    level = 0
    k = -1

    while q:

        level += 1

        for _ in range(len(q)):
            row, col = q.popleft()

            distance[row][col] = level

            if row == goal[0] and col == goal[1]:
                k = level

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not inbound(nr, nc):
                    continue

                if grid[nr][nc] == "#":
                    continue

                if visited[nr][nc]:
                    continue

                visited[nr][nc] = True

                q.append((nr, nc))

    if k == -1:
        return print("Tie")

    for i in range(n):
        for j in range(m):
            if (not visited[i][j] and grid[i][j] != "#") or distance[i][j] > k:
                return print("Kibr")

    return print("Ludis")


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

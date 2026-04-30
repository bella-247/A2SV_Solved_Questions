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


from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


# sys.setrecursionlimit(200000) # don't forget to use python 3

def solution(_):
    n = ri()
    q = rls()
    k = rls()
    goal = rls()

    for i in range(2):
        q[i] -= 1
        k[i] -= 1
        goal[i] -= 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    grid = [[1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i + j == q[0] + q[1]:
                grid[i][j] = 0

            if i - j == q[0] - q[1]:
                grid[i][j] = 0

            if i == q[0] and j != q[1]:
                grid[i][j] = 0

            if i != q[0] and j == q[1]:
                grid[i][j] = 0

    grid[k[0]][k[1]] = 0
    stack = [k]

    while stack:
        row, col = stack.pop()

        if row == goal[0] and col == goal[1]:
            return yn(1)

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if not (-1 < nr < n and -1 < nc < n):
                continue

            if grid[nr][nc] == 0:
                continue

            grid[nr][nc] = 0

            stack.append([nr, nc])

    yn(0)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

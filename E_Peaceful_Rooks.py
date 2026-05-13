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


sys.setrecursionlimit(200000)  # don't forget to use python 3


def solution(_):
    n, m = rls()

    adj = [-1] * (n + 1)

    rooks = [rls() for _ in range(m)]

    rooks = list(filter(lambda x: x[0] != x[1], rooks))

    rows = set(r for r, c in rooks)

    indeg = [0] * (n + 1)

    for r, c in rooks:
        if c not in rows:
            continue

        adj[r] = c
        indeg[c] += 1

    q = deque()

    for r, c in rooks:
        if indeg[r] == 0:
            q.append(r)

    moves = 0

    while q:
        moves += 1

        v = q.popleft()

        next = adj[v]

        if next == -1:
            continue

        indeg[next] -= 1

        q.append(next)

    visited = [False] * (n + 1)

    def cycleDepth(ver):
        nodes = 0

        stack = [ver]
        visited[ver] = True

        while stack:
            v = stack.pop()

            nodes += 1

            next = adj[v]

            if not visited[next]:
                visited[next] = True
                stack.append(next)

        return nodes

    for r in rows:
        if indeg[r] != 0 and not visited[r]:
            moves += cycleDepth(r) + 1

    print(moves)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

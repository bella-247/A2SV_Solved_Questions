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

# sys.setrecursionlimit(200000)  # don't forget to use python 3

def solution(_):
    n, m = rls()

    adj = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        u, v = rls()
        adj[u].append(v)
        adj[v].append(u)

    def bfs():
        path = []
        visited[1] = True
        heap = [1]

        while heap:
            v = heappop(heap)
            path.append(v)

            for nei in adj[v]:
                if not visited[nei]:
                    visited[nei] = True
                    heappush(heap, nei)

        return path

    print(*bfs())


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

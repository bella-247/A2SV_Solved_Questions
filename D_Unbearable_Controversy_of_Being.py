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


def summation(n):
    if n <= 0:
        return 0
    return (n * (n + 1)) // 2


# sys.setrecursionlimit(200000) # don't forget to use python 3


def solution(_):
    n, m = rls()

    adj = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        u, v = rls()
        adj[u].append(v)

    def counter(v):
        counts = Counter()

        for nei in adj[v]:
            for neigh in adj[nei]:
                
                if neigh != v:
                    counts[neigh] += 1

        total = 0

        for count in counts.values():
            total += summation(count - 1)

        return total

    def dfs(vertex):
        count = 0
        stack = [vertex]

        while stack:
            v = stack.pop()
            count += counter(v)

            for nei in adj[v]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)

        return count

    total = 0

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            total += dfs(i)

    print(total)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

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


def ris(splitor=" "):
    return map(int, rs().split(splitor))


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
    n, m = ris()
    costs = [0] + rls()

    adj = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        u, v = rls()
        adj[u].append(v)
        adj[v].append(u)

    def dfs(vertex):
        minn = costs[vertex]

        for nei in adj[vertex]:
            if visited[nei]:
                continue

            visited[nei] = True
            minn = min(minn, dfs(nei))

        return minn

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

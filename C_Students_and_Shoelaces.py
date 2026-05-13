import random, math, sys, heapq as heap
from itertools import accumulate
from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from random import randint
from heapq import heapify, heappush, heappop
from tokenize import group

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

    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)

    for _ in range(m):
        u, v = rls()
        adj[u].append(v)
        adj[v].append(u)
        indeg[u] += 1
        indeg[v] += 1

    q = deque()

    for i in range(1, n + 1):
        if indeg[i] == 1:
            q.append(i)

    groups = 0

    while q:
        k = len(q)
        free = False

        for _ in range(k):
            v = q.popleft()
        
            if indeg[v] == 0:
                continue

            free = True

            for nei in adj[v]:
                indeg[nei] -= 1

                if indeg[nei] == 1:
                    q.append(nei)

        groups += int(free)

    print(groups)
    

def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

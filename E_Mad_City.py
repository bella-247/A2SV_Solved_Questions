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
    print("YES" if res else "NO")


def acc(arr):
    return list(accumulate(arr))


rand = random.getrandbits(32)


def xor(x):
    return x ^ rand


# sys.setrecursionlimit(200000) # don't forget to use python 3


def solution(_):
    n, a, b = rls()

    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)

    for _ in range(n):
        u, v = rls()
        adj[u].append(v)
        adj[v].append(u)

        indeg[v] += 1
        indeg[u] += 1


    q = deque()
    
    for i in range(1, n + 1):
        if indeg[i] == 1:
            q.append(i)
    
    
    while q:
        v = q.popleft()

        for nei in adj[v]:
            indeg[nei] -= 1

            if indeg[nei] == 1:
                q.append(nei)


    visited = [False] * (n + 1)
    visited[a] = True

    # me
    q = deque([b])
    my_distances = [inf] * (n + 1)
    dis = -1

    while q:
        dis += 1

        for _ in range(len(q)):
            v = q.popleft()
            my_distances[v] = dis

            for nei in adj[v]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

    visited = [False] * (n + 1)
    visited[b] = True
    
    # friend
    q = deque([a])
    fr_distances = [inf] * (n + 1)
    dis = -1

    while q:
        dis += 1

        for _ in range(len(q)):
            v = q.popleft()
            fr_distances[v] = dis

            for nei in adj[v]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

    for i in range(1, n + 1):
        if indeg[i] > 1 and my_distances[i] < fr_distances[i]:
            return yn(1)

    yn(0)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

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
    n, m, s, t = rls()

    adj = [set() for _ in range(n + 1)]

    for _ in range(m):
        u, v = rls()
        adj[u].add(v)
        adj[v].add(u)

    def bfs(start):
        visited = [False] * (n + 1)
        q = deque([start])
        visited[start] = True

        distance = [inf] * (n + 1)
        level = 0

        while q:
            for _ in range(len(q)):
                v = q.popleft()
                distance[v] = level

                for nei in adj[v]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)

            level += 1

        return distance

    distance_t = bfs(t)
    distance_s = bfs(s)

    target = distance_s[t]
    count = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or j in adj[i]:
                continue

            path = min(distance_s[i] + distance_t[j], distance_s[j] + distance_t[i]) + 1

            if path >= target:
                count += 1

    print(count // 2)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

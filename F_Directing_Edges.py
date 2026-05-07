from os import umask
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


sys.setrecursionlimit(200000)  # don't forget to use python 3


def solution(_):
    n, m = rls()

    adj = [set() for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    outdeg = [0] * (n + 1)
    visited = [0] * (n + 1)

    undirected = set()

    for _ in range(m):
        t, u, v = rls()
        adj[u].add(v)
        if t == 2:
            undirected.add((u, v))
            adj[v].add(u)

        if t == 1:
            indeg[v] += 1
            outdeg[u] += 1

    def has_cycle(v):
        for nei in adj[v]:
            if visited[nei] == 1:
                return True
            
            elif visited[nei] == 0:
                visited[nei] = 1
                if (v, nei) not in undirected or (nei, v) not in undirected and has_cycle(nei):
                    return True
                
        
        visited[v] = 2
        return False


    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            if has_cycle(i):
                return yn(0)

    for u,v in undirected:
        inn = indeg[u] > 0

        if inn:
            for nei in adj[u]:
                if (nei, u) in undirected or (u, nei) in undirected:
                    indeg[nei] -= 1
                    adj[u].remove(nei)
        # out
        else:
            for nei in adj[u]:
                if (nei, u) in undirected or (u, nei) in undirected:
                    indeg[nei] += 1
                    adj[nei].remove(u)

    yn(1)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

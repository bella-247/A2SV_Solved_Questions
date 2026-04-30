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


# sys.setrecursionlimit(200000) # don't forget to use python 3


def solution(_):
    n, m = rls()

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = rls()
        adj[v].append(u)
        adj[u].append(v)
        
    def isRoot(start, graph):
        visited = [False] * (n + 1)
        visited[start] = True
        
        level = 0
        queue = deque([start])
        
        while queue:
            level += 1
            
            if level > 3:
                return False
            
            for i in range(len(queue)):
                vertex = queue.popleft()
                
                for nei in graph[vertex]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)
        
        return True

    
    for i in range(1, n+1):
        if isRoot(i, adj):
            x = len(adj[i])
            nei = adj[i].pop()
            y = len(adj[nei]) - 1

            return print(x, y)

def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

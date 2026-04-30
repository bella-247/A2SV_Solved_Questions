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
    n = ri()
    nums = rls()

    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    
    for i in range(1, n + 1):
        adj[i].append(nums[i - 1])
        indeg[nums[i - 1]] += 1

    q = deque()

    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    year = 2
    
    while q:
        year += 1
        
        for _ in range(len(q)):
            v = q.popleft()

            for nei in adj[v]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

    print(year)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

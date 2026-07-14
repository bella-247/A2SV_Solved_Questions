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

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n + 1))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def erase(self, x):
        self.root[x] = self.find(x + 1)
        
def solution(_):
    n = ri()
    a = rls()

    suf = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1] + a[i]

    uf = UnionFind(n)

    ans = 0

    for i in range(n - 1, -1, -1):
        j = i + 1

        while j < n:
            cur = suf[i] - suf[j]

            if a[j] >= cur:
                break

            uf.erase(j)
            j = uf.find(j)

        ans = max(ans, suf[i] - suf[j])

    print(ans)
    
def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

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
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.root[ry] = rx
        self.size[rx] += self.size[ry]

        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def solution(_):
    n, x, y = rls()
    nums = rls()

    uf = UnionFind(n)

    for i in range(1, n + 1):
        if i + x <= n:
            uf.union(i, i + x)
        if i + y <= n:
            uf.union(i, i + y)

    for i in range(n):
        current_pos = i + 1
        target_pos = nums[i]

        if not uf.connected(current_pos, target_pos):
            return yn(0)

    yn(1)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

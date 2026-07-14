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


class UnionFind:
    def __init__(self):
        self.root = {}
        self.size = {}

    def setRoot(self, lang):
        if lang in self.root:
            return

        self.root[lang] = lang
        self.size[lang] = 1

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
    n, m = rls()
    languages = [rls() for _ in range(n)]

    uf = UnionFind()

    non = 0

    for k, *langs in languages:
        if k == 0:
            non += 1

        for lang in langs:
            uf.setRoot(lang)
            uf.union(langs[0], lang)

    comps = set()

    for lang in uf.root:
        comps.add(uf.find(lang))

    print(non + max(0, len(comps) - 1))


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

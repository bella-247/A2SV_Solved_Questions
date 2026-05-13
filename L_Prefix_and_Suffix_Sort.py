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


def solution(_):
    n = ri()

    nums = rls()
    indexed = [(num, i) for i, num in enumerate(nums)]
    sorted_indexed = sorted(indexed)
    mapp = [-1] * n

    for i in range(n):
        tup = sorted_indexed[i]
        mapp[tup[1]] = i

    maxx = 0

    def close(i):
        return 0 if i <= n - i - 1 else n - 1

    for i in range(n):
        sorted_index = mapp[i]
        if i == sorted_index:
            continue

        diff = abs(i - close(sorted_index))

        maxx = max(maxx, diff + 1)

    print(maxx)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

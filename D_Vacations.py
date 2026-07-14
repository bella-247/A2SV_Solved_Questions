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

    memo = {}

    def dp(i, prev):
        if i == n:
            return 0

        if (i, prev) in memo:
            return memo[(i, prev)]

        if nums[i] == 0:
            memo[(i, prev)] = 1 + dp(i + 1, nums[i])

        if nums[i] == 1:
            if prev == 1:
                memo[(i, prev)] = 1 + dp(i + 1, 0)
            else:
                memo[(i, prev)] = dp(i + 1, 1)

        if nums[i] == 2:
            if prev == 2:
                memo[(i, prev)] = 1 + dp(i + 1, 0)
            else:
                memo[(i, prev)] = dp(i + 1, 2)

        if nums[i] == 3:
            one = dp(i + 1, 2) if prev == 1 else dp(i + 1, 1)
            two = dp(i + 1, 1) if prev == 2 else dp(i + 1, 2)

            memo[(i, prev)] = min(one, two)

        return memo[(i, prev)]

    print(dp(0, 0))


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

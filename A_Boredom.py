from operator import countOf
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

# sys.setrecursionlimit(200000)  # don't forget to use python 3


def solution(_):
    n = ri()
    nums = rls()

    counts = Counter(nums)
    nums = sorted(counts)
    n = len(nums)

    memo = [-1] * n

    def dp(i):
        if i >= n:
            return 0

        if memo[i] != -1:
            return memo[i]

        best = nums[i] * counts[nums[i]]

        if i < n - 1 and nums[i + 1] != nums[i] + 1:
            best += dp(i + 1)

        else:
            best += max(dp(i + 2), dp(i + 3))

        memo[i] = best

        return memo[i]

    return print(max(dp(0), dp(1)))


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

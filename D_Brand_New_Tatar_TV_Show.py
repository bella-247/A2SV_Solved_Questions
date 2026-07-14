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
    n, k = rls()

    nums = rls()
    counts = Counter(nums)
    nums = sorted(counts)
    print(nums)

    if n == 1:
        return yn(0)

    for i in range(1, len(nums)):
        if i > 0:
            if nums[i - 1] - nums[i] > k and counts[nums[i]] % 2 == 0:
                return yn(1)
            
        elif i > 
                
        if i < 2 or (nums[i - 1] - nums[i] <= k and nums[i - 2] - nums[i - 1] > k):
            prev = counts[i - 1] if i > 0 else 0

            if (counts[nums[i]] + prev) % 2 == 0:
                return yn(1)

        yn(0)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

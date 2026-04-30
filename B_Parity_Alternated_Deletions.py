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
    n = ri()
    nums = rls()
    nums.sort(reverse=True)
    total = sum(nums)

    groups = {0: [], 1: []}

    summ = 0

    for num in nums:
        groups[num % 2].append(num)

    i = 0
    j = 0

    end = min(len(groups[0]), len(groups[1]))

    summ = sum(groups[0][:end]) + sum(groups[1][:end])

    if end < len(groups[0]):
        summ += groups[0][end]

    if end < len(groups[1]):
        summ += groups[1][end]

    print(total - summ)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

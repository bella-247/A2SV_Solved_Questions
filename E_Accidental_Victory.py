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


rand = random.getrandbits(32)


def xor(x):
    return x ^ rand


# sys.setrecursionlimit(200000) # don't forget to use python 3


def solution(_):
    n = ri()

    nums = rls()
    indexed = sorted((num, i) for i, num in enumerate(nums))

    # -- Prepare for computation
    prefix = []
    p = 0
    for num, index in indexed:
        p += num
        prefix.append(p)
    # -- Prepare for computation

    # validity checker
    def checker(index):
        if index < 0:
            return False

        if index == n:
            return True

        for i in range(index + 1, n):
            if prefix[i - 1] < indexed[i][0]:
                return False

        return True

    # find the starting valid point
    left = 0
    right = n - 2

    while left <= right:

        mid = left + (right - left) // 2

        if checker(mid):
            right = mid - 1

        else:
            left = mid + 1

    # final result
    result = []
    for i in range(left, n):
        result.append(indexed[i][1] + 1)

    result.sort()
    print(len(result))
    print(*result)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

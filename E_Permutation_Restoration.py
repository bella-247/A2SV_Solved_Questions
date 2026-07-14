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
    n = ri()
    nums = rls()

    def rangee(index, num):
        pos = index + 1
        if num == 0:
            return [n, pos + 1, index]

        upper = pos // num
        lower = pos // (num + 1) + 1

        return [upper, lower, index]

    intervals = []

    for i in range(n):
        intervals.append(rangee(i, nums[i]))

    intervals.sort()
    # print(intervals)
    num = 1
    for _, __, index in intervals:
        nums[index] = num
        num += 1

    print(*nums)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

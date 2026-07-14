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


def C1(index, arr):
    if index == -1:
        return []

    flipped = False
    actions = []

    for i in range(index - 1, -1, -1):
        if flipped and arr[i] < 0:
            actions.append(i + 1)
            flipped = not flipped
        elif not flipped and arr[i] > 0:
            actions.append(i + 1)
            flipped = not flipped

    return actions + [index + 1]


INF = 10**18


def solution(_):
    n = ri()
    nums = rls()

    prefix = [0]

    for i in range(n):
        prefix.append(prefix[-1] + abs(nums[i]))

    suffix = [0] * (n + 1)

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + nums[i + 1]

    maxx = sum(nums)
    max_index = -1

    for i in range(n):
        if nums[i] > 0:
            res = prefix[i] + suffix[i] - nums[i]
            if res > maxx:
                maxx = res
                max_index = i

    result = C1(max_index, nums)
    print(len(result))
    print(*result)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()


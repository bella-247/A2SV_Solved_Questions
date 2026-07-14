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


def best(intervals, start):
    inter = None
    starting_index = bisect_left(intervals, [-inf, start, -inf])

    for i in range(starting_index, len(intervals)):
        interval = intervals[i]
        if interval[0] <= start <= interval[1]:
            if not inter:
                inter = interval

            elif inter[1] < interval[1]:
                inter = interval

        elif interval[0] > start:
            break

    return inter


def toInterval(sub, index, string):
    intervals = []

    if sub not in string:
        return []

    n, k = len(string), len(sub)

    for i in range(n - k + 1):
        if string[i : i + k] == sub:
            intervals.append([i, i + k - 1, index])

    return intervals


def solution(_):
    t = rs()
    m = len(t)
    n = ri()
    seals = [rs() for _ in range(n)]

    intervals = []

    for i, seal in enumerate(seals):
        intervals.extend(toInterval(seal, i, t))

    intervals.sort()

    result = []

    covered = -1
    while covered < m - 1:
        interval = best(intervals, covered + 1)
        if not interval:
            return print(-1)

        start, end, index = interval

        covered = end
        result.append([index + 1, start + 1])

    print(len(result))
    for res in result:
        print(*res)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

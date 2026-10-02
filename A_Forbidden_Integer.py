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
    n, k, x = rls()

    result = []

    if k == 1:
        return yn(0)

    if x != 1:
        result = [1] * n

    elif n % 2 == 0:
        result = [2] * (n // 2)

    elif k >= 3:
        two = (n - 2) // 2
        result = [2] * two
        result.append(3)

    if result:
        yn(1)
        print(len(result))
        print(*result)

    else:
        yn(0)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

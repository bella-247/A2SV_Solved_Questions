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
    s = rs()

    count = 0

    if n == 1:
        return print(1 if s[0] == "x" else 0)

    for i in range(n):
        if s[i] == "x":
            if i == 0 and s[i + 1] == "x":
                count += 1

            elif i == n - 1 and s[i - 1] == "x":
                count += 1

            elif 0 < i < n - 1 and s[i - 1] == "x" and s[i + 1] == "x":
                count += 1

    print(count)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

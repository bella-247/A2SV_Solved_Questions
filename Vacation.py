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


sys.setrecursionlimit(200000)  # don't forget to use python 3

INF = 10**18


def solution(_):
    n = ri()
    days = [rls() for _ in range(n)]

    memo = [[0] * 3 for _ in range(n)]

    for i in range(3):
        memo[n - 1][i] = days[n - 1][i]

    for i in range(n - 2, -1, -1):
        next = i + 1

        for j in range(3):
            memo[i][j] = days[i][j] + max(memo[next][k] for k in range(3) if k != j)

    print(max(memo[0]))


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

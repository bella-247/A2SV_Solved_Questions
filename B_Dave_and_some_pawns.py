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

    enemy = list(rs())
    dave = list(rs())

    count = 0
    for i in range(n):
        if dave[i] == "0":
            continue

        if enemy[i] == "0":
            count += 1
            enemy[i] = "-"
            continue

        if i > 0 and enemy[i - 1] == "1":
            count += 1
            enemy[i - 1] = "-"

        elif i < n - 1 and enemy[i + 1] == "1":
            count += 1
            enemy[i + 1] = "-"

    print(count)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

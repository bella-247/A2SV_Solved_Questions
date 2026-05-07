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
    print("YES" if res else "NO")


def acc(arr):
    return list(accumulate(arr))


rand = random.getrandbits(32)


def xor(x):
    return x ^ rand


# sys.setrecursionlimit(200000) # don't forget to use python 3


def solution(_):
    n, k = rls()

    if n % 2 != 0 and k % 2 == 0:
        return yn(0)

    x = (n + k - 1) // k

    rem = x * k - n

    if rem % 2 != 0:
        x += 1
        rem = x * k - n

    if rem % 2 != 0:
        return yn(0)

    result = []
    for _ in range(k):
        minn = min(2, rem)

        if x - minn <= 0:
            return yn(0)

        result.append(x - minn)
        
        rem -= minn

    yn(1)
    print(*result)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

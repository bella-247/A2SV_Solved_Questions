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


def solution(_):
    r1, c1, r2, c2 = rls()

    rook = 1 if r1 == r2 or c1 == c2 else 2

    diff1 = r1 - c1
    diff2 = r2 - c2

    if diff1 % 2 != diff2 % 2:
        bishop = 0

    else:
        sum1 = r1 + c1
        sum2 = r2 + c2
        bishop = 1 if diff1 == diff2 or sum1 == sum2 else 2

    king = max(abs(r1- r2), abs(c1 - c2))
    
    print(rook, bishop, king)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

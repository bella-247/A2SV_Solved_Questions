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
    nums = list(map(int, list(rs())))

    ignis = [nums[i] for i in range(0, n, 2)]
    aqua = [nums[i] for i in range(1, n, 2)]

    ignis.sort(key=lambda x: x % 2, reverse=True)
    aqua.sort(key=lambda x: x % 2, reverse=False)

    turn = 0
    for i in range(n - 1):
        if turn == 0:
            ignis.pop()

        else:
            aqua.pop()

        turn = 1 - turn

    x = ignis.pop() if ignis else aqua.pop()
    
    print(1 if x % 2 != 0 else 2)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

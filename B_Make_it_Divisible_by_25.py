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
    s = str(n)
    n = len(s)

    minn = inf
    for i in range(n - 1, -1, -1):
        if s[i] != "0" and s[i] != "5":
            continue

        for j in range(i - 1, -1, -1):
            if s[i] == "0" and s[j] in ["0", "5"]:
                minn = min(minn, n - j - 2)
                break
            elif s[i] == "5" and s[j] in ["2", "7"]:
                minn = min(minn, n - j - 2)
                break

    print(minn)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

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
    a = rls()
    b = rls()

    sorted_a = sorted(a)

    for i in range(n):
        smalls = bisect_right(sorted_a, b[i])

        if smalls < i + 1:
            return print(-1)

    total = 0

    for i in range(n):
        if a[i] <= b[i]:
            continue

        index = -1
        for j in range(i + 1, n):
            if a[j] <= b[i]:
                index = j
                break

        a.insert(i, a.pop(index))
        total += abs(index - i)

    print(total)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

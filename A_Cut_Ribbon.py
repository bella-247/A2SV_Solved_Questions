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
    n, a, b, c = rls()

    state = [-inf] * (4001)
    state[a] = state[b] = state[c] = 1

    for i in range(1, n + 1):
        maxx = state[i]

        if i - a > 0:
            maxx = max(maxx, state[i - a] + 1)

        if i - b > 0:
            maxx = max(maxx, state[i - b] + 1)

        if i - c > 0:
            maxx = max(maxx, state[i - c] + 1)

        state[i] = maxx

    print(state[n])


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

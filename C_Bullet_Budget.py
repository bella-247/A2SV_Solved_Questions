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
    n, k = rls()

    health = rls()
    positions = rls()

    beasts = [[h, abs(p)] for h, p in zip(health, positions)]
    beasts.sort(key=lambda beast: beast[1])
    beasts = deque(beasts)

    steps = 0

    while beasts and beasts[0][1] - steps > 0:
        shots = k

        # shots
        while beasts and shots > 0:
            bullet = min(shots, beasts[0][0])

            beasts[0][0] -= bullet

            if beasts[0][0] == 0:
                beasts.popleft()

            shots = shots - bullet

        steps += 1

    yn(len(beasts) == 0)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

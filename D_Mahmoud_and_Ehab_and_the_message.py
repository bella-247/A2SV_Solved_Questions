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
    n, k, m = rls()

    words = rs().split()
    costs = rls()

    groups = {}

    group_min = [inf] * k

    for i in range(k):
        x, *arr = rls()

        for j in range(x):
            index = arr[j] - 1
            word = words[index]
            groups[word] = i
            group_min[i] = min(group_min[i], costs[index])


    # final answer

    total = 0

    used = rs().split()

    for word in used:
        g = groups[word]
        total += group_min[g]

    print(total)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

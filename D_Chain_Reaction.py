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
    a, b = rls()
    s = rs()
    n = len(s)
    nums = list(map(int, list(s)))

    stack = []

    left = 0
    for right in range(n):
        if nums[right] == 0:
            left = right + 1

        elif stack and stack[-1][0] == left:
            stack.pop()
            stack.append([left, right])

        else:
            stack.append([left, right])

    k = len(stack)

    cost = a if k > 0 else 0

    for i in range(1, k):
        gap = stack[i][0] - stack[i - 1][1] - 1
        cost += min(gap * b, a)

    print(cost)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

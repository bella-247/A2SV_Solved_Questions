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
    nums = rls()
    n = len(nums)

    prefix = [nums[0]]
    acc = 0

    for i in range(1, n):
        if nums[i] >= prefix[-1]:
            prefix.append(prefix[-1])
            acc += nums[i] - prefix[-1]

        else:
            
            summ = prefix[-1] * i + min(prefix[-1], nums[i] + acc)
            new = summ // (i + 1)
            acc -= max(0, new - nums[i])
            acc += max(0, prefix[-1] - new) * i
            prefix.append(new)

    print(*prefix)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

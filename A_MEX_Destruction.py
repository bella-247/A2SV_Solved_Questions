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


def continous(arr):
    if arr[0] != 0:
        return False

    for i in range(1, len(arr)):
        if arr[i] == 0 and arr[i - 1] != 0:
            return False
    return True


def solution(_):
    n = ri()
    nums = rls()

    count = nums.count(0)

    if count == n:
        return print(0)

    if count == 0:
        return print(1)

    left = -1
    right = n

    for i in range(n):
        if nums[i] != 0:
            break
        
        left = i
            
    for i in range(n - 1, -1, -1):
        if nums[i] != 0:
            break
        right = i

    print(2 if 0 in nums[left + 1 : right] else 1)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

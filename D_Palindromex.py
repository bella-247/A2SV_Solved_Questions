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


def isPalindrome(arr):
    n = len(arr)
    i = 0
    j = n - 1

    while i < j:
        if arr[i] != arr[j]:
            return False

        i += 1
        j -= 1

    return True


def mex(arr):
    nums = set(arr)
    for i in range(len(arr) + 1):
        if i not in nums:
            return i

    return len(arr) + 1


def solution(_):
    n = ri()
    n = 2 * n
    nums = rls()

    z1 = -1
    z2 = -1

    for i in range(n):
        if nums[i] == 0:
            if z1 == -1:
                z1 = i
            else:
                z2 = i

    maxx = 1

    if isPalindrome(nums[z1 : z2 + 1]):
        i = z1
        j = z2

        while i > -1 and j < n and nums[i] == nums[j]:
            i -= 1
            j += 1

        maxx = max(maxx, mex(nums[i + 1 : j]))

    else:
        i = z1
        j = z1

        while i > -1 and j < n and nums[i] == nums[j]:
            i -= 1
            j += 1

        maxx = max(maxx, mex(nums[i + 1 : j]))

        i = z2
        j = z2

        while i > -1 and j < n and nums[i] == nums[j]:
            i -= 1
            j += 1

        maxx = max(maxx, mex(nums[i + 1 : j]))

    print(maxx)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

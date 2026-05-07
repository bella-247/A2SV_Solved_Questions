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


def mex(arr):
    n = len(arr)
    arr = set(arr)

    for i in range(n + 1):
        if i not in arr:
            return i

    return -1


def solution(_):
    n = ri()

    nums = rls()
    nums.sort()
    
    nums_set = set(nums)
    
    longest = 0
    for i in range(n):
        
        if nums[i] - 1 in nums_set:
            continue
        
        count = 1
        num = nums[i]
        while num + 1 in nums_set:
            count += 1
            num += 1
        
        longest = max(longest, count)
        
    print(longest)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

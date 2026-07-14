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
    n = ri()

    nums = rls()
    sorted_nums = sorted(nums)

    indices = defaultdict(set)
    
    for i in range(n):
        indices[sorted_nums[i]].add(i)
    
    swaps = []
    
    for i in range(n):
        while i not in indices[nums[i]]:
            for index in indices[nums[i]]:
                if nums[index] != sorted_nums[index]:
                    swaps.append([i, index])
                    nums[i], nums[index] = nums[index], nums[i]
                    break
    
    print(len(swaps))
    
    for swap in swaps:
        print(*swap)

def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

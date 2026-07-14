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
    
    edges = []
    
    prefix = [nums[0]]
    
    for i in range(1, n):
        prefix.append(min(nums[i], prefix[-1]))
    
    maxx = nums[-1]
    
    for i in range(n - 1, 0, -1):
        maxx = max(maxx, nums[i])
        
        if maxx < prefix[i - 1]:
            return yn(0)
        
        if maxx > nums[i - 1]:
            edges.append([maxx, nums[i - 1]])
            
        else:
            edges.append([maxx, prefix[i - 1]])
        
    
    yn(1)
    for u, v in edges:
        print(u, v)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()


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
    s = rs()
    s = [c if c != "3" else "1" for c in s]
    n = len(s)
    
    count = s.count("4")
    
    left = 0
    right = -1
    
    while left < n and s[left] != "1":
        left += 1
        
    right = n - 1
    while right > -1 and s[right] != "2":
        right -= 1
    
    s = s[left : right + 1]
    
    counts = Counter(s)
    
    
    
    for i in range(n):
        if not stack or stack[-1][0] != s[i]:
            stack.append([s[i], 1])
        else:
            stack[-1][1] += 1
            
    print(count)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

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

def rs(): return input().strip()
def ri(): return int(rs())
def rls(spliter=" "): return list(map(int, rs().split(spliter)))
def yn(res): print("YES" if res else "NO")

def acc(arr): return list(accumulate(arr))
rand = random.getrandbits(32)
def xor(x): return x ^ rand 

# sys.setrecursionlimit(200000) # don't forget to use python 3

def sumAll(n):
    return (n * (n + 1)) // 2

def solution(_):
    n, m = rls()
    
    x = n // m
    y = x + 1
    
    l2 = n - m*x
    l1 = m - l2
    
    minn = l1 * sumAll(x - 1) + l2 * sumAll(y - 1)
    
    x = n - (m - 1)
    maxx = sumAll(x - 1)
    
    print(minn, maxx)

def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

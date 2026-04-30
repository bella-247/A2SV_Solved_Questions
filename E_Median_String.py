import random, math, sys, heapq as heap
from itertools import accumulate
from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from random import randint

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
def digits(num):
    return math.log10(num if num >= 1 else 1) + 1

def add(a, b, carry):
    return divmod(a + b + carry, 26)

def subtract(a, b, borrow):
    a -= borrow
    bor = 0
    
    if a < b:
        a = a + 26
        bor = 1
    
    res = a - b
    
    return res, bor

def division(num, passed):
    # if num == 1
    pass

def solution(_):
    pass
    

def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

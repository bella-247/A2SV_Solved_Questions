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

def solution(_):

    one = rs()
    two = rs()
    n = len(one)
    
    result = []
    
    for i in range(n):
        result.append("1" if one[i] != two[i] else "0")
        
    print("".join(result))

def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

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
    n, m = rls()
    
    result = [["." for _ in range(m)] for _ in range(n)]

    for i in range(0, n, 2):
        for j in range(m):
            result[i][j] = "#"
    
    left = False
    for i in range(1, n, 2):
        if left:
            result[i][0] = "#"
        else:
            result[i][m - 1] = "#"
            
        left = not left
    
    for row in result:
        print("".join(row))

def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

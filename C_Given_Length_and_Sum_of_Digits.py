import string
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

def stringify(arr):
    return "".join(map(str, arr))


def solution(_):
    m, s = rls()
    
    digits = [9] * m
    
    maxx = 9 * m
    
    if s > maxx:
        return print(-1, -1)
    
    if s == 0 and m > 1:
        return print(-1, -1)
    

    
    maximum = stringify(digits)
    
    s -= 1
    
    digits = [0] * m
    
    i = 0
    while s > 0:
        if s > 9:
            digits[i] = 9
            
        else:
            digits[i] = s
            
        i += 1
    
    digits[-1] += 1
    
    minimum = stringify(digits)
    print(minimum, maximum)
    
    
def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

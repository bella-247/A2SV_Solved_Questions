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
    n = ri()
    nums = rls()
    nums.sort()
    
    inc = []
    dec = []
    
    for num in nums:
        if not inc or inc[-1] != num:
            inc.append(num)
        
        elif not dec or dec[-1] != num:
            dec.append(num)
            
        else:
            return yn(0)
        
    dec.reverse()
    
    yn(1)
    print(len(inc))
    print(*inc)
    
    print(len(dec))
    print(*dec)
    
    


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

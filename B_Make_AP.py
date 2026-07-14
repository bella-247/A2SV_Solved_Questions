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

INF = 10**18
def solution(_):
    a, b, c = rls()
    
    d = b - a
    need = b + d

    if need > 0 and c <= abs(need) and need % c == 0:
        return yn(1)

    d = c - b
    need = b - d

    if need > 0 and a <= abs(need) and need % a == 0:
        return yn(1)

    d = c - a

    if d % 2 != 0:
        return yn(0)

    need = a + (d // 2)

    if d % 2 == 0 and need > 0 and b <= abs(need) and need % b == 0:
        return yn(1)

    yn(0)






def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

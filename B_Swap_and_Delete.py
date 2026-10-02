import random, math, sys, heapq as heap
from itertools import accumulate
from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from random import randint
from heapq import heapify, heappush, heappop, heapreplace

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
    s = rs()
    n = len(s)
    counts = Counter(s)

    for i in range(n):
        if s[i] == "0" and counts["1"] > 0:
            counts["1"] -= 1
        elif s[i] == "1" and counts["0"] > 0:
            counts["0"] -= 1

        else:
            return print(n - i)

    print(0)


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

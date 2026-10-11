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

    map = defaultdict(int)

    n = ri()
    s = rs()

    if s == "0":
        return print(1)

    if s[0] == "0":
        return print(sum(int(s[i] != "0") for i in range(n)))

    count = 0

    for i in range(n):
        for k, v in map.items():
            if k != s[i]:
                count += v

        if s[i] == "0":
            count -= 1

        map[s[i]] += 1


    print(count + 1)









def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

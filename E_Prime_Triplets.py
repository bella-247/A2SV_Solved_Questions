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

# Time: O(N log log N) | Space: O(N)
def get_is_prime(n):
    is_prime = bytearray([1]) * (n + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, isqrt(n) + 1):
        if is_prime[i]:
            is_prime[i*i : n+1 : i] = bytearray((n - i*i) // i + 1)
    return is_prime

is_prime = get_is_prime(10**6 + 10)


def solution(_):
    a, b = rls()

    count = 0

    if a % 2 == 0:
        a += 1

    for i in range(a, b, 2):
        m2, m4 = i - 2, i - 4
        p2, p4 = i + 2, i + 4

        if not is_prime[i]:
            continue

        if m2 >= a and p4 <= b and is_prime[m2] and is_prime[p4]:
            count += 1
            
        if m4 >= a and p2 <= b and is_prime[m4] and is_prime[p2]:
            count += 1

    print(count)



def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()







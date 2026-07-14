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
def getId(x):
    count = Counter(str(x))
    id = []
    for i in range(1,10):
        I = str(i)
        id.append(I)
        id.append(str(count[I]))
    return "".join(id)

def solution(_):
    s, p = rls()
    ans = []
    
    q = deque([(0,0,1)])
    visited = set()
    visited.add(getId(q[0]))
    while q:
        new_q = deque()
        for num in q:
            n, sm, pr = num
            
            for i in range(1,10):
                new_n = n*10 + i
                id = getId(new_n)
                print(id)
                if id in visited or sm + i > s or pr * i > p:
                    continue
                if sm + i > 120 or pr * i > 10**18:
                    continue
                if sm +i == s and pr * i == p:
                    ans = new_n
                visited.add(i)
                new_q.append((new_n, sm + i, pr * i))
        if ans:
            break
        q = new_q
    if ans:
        ans = sorted(list(str(ans)))
        print("".join(ans))
    else:
        print(-1)

def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()

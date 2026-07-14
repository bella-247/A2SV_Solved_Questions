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


def rs():
    return input().strip()


def ri():
    return int(rs())


def rls(spliter=" "):
    return list(map(int, rs().split(spliter)))


def yn(res):
    print("YES" if res else "NO")


def acc(arr):
    return list(accumulate(arr))


rand = random.getrandbits(32)


def xor(x):
    return x ^ rand


# sys.setrecursionlimit(200000) # don't forget to use python 3


def solution(_):
    n, m = rls()

    s = rs()

    west = deque()
    east = deque()

    w = True
    e = True

    for i in range(n):
        if s[i] == "[":
            w = not w
            continue

        if s[i] == "]":
            e = not e
            continue

        if s[i] == "<":
            if west:
                west.pop()

            elif east:
                east.popleft()

            continue

        elif s[i] == ">":
            if east:
                east.pop()

            elif west:
                west.popleft()

            continue

        if len(west) + len(east) == m:
            continue

        if e:
            east.append(i)

        elif w:
            west.append(i)
    
    while west:
        print(s[west.pop()], end="")

    while east:
        print(s[east.popleft()], end="")

    print()


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

import random, math, sys, heapq as heap
from itertools import accumulate
from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from random import randint

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


def fix(s, counts, pairs):
    n = len(s)

    i = 0
    j = n - 1

    while i < j:
        if s[i] == "?" and s[j] == "?":
            pairs.append((i, j))

        elif s[i] == "?":
            s[i] = s[j]

        elif s[j] == "?":
            s[j] = s[i]
            
        elif s[i] != s[j]:
            return False

        counts[s[i]] -= 1
        counts[s[j]] -= 1

        if s[i] != "?" and counts[s[i]] < 0:
            return False

        i += 1
        j -= 1


    if n % 2 != 0:
        counts[s[n // 2]] -= 1

    return counts["0"] >= 0 and counts["1"] >= 0


def solution(_):
    a, b = rls()
    s = list(rs())
    n = len(s)
    
    mid = n // 2

    counts = defaultdict(int)
    counts["0"] = a
    counts["1"] = b

    pairs = []

    if not fix(s, counts, pairs):
        return print(-1)

    for i, j in pairs:
        if counts["0"] >= 2:
            s[i] = "0"
            s[j] = "0"
            counts["0"] -= 2

        elif counts["1"] >= 2:
            s[i] = "1"
            s[j] = "1"
            counts["1"] -= 2

        else:
            return print(-1)

    if n % 2 != 0 and s[mid] == "?":
        if counts["0"] < 1 and counts["1"] < 1:
            return print(-1)

        s[mid] = "0" if counts["0"] > 0 else "1"
        counts[s[mid]] -= 1

    if not (counts["0"] == 0 and counts["1"] == 0):
        return print(-1)

    else:
        print("".join(s))


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

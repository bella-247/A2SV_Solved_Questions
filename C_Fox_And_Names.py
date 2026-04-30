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


def compare(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return a[i], b[i]

    return (None, None) if len(a) > len(b) else ("", "")


def solution(_):
    n = ri()
    names = [rs() for _ in range(n)]
    adj = defaultdict(list)
    indegree = Counter()

    for i in range(n):
        seen = set()

        for j in range(i + 1, n):
            u, v = compare(names[i], names[j])
            if u is None:
                return print("Impossible")

            if v not in seen:
                adj[u].append(v)
                indegree[v] += 1

    q = deque()

    for c in "abcdefghijklmnopqrstuvwxyz":
        if indegree[c] == 0:
            q.append(c)

    result = []
    while q:
        c = q.popleft()
        result.append(c)

        for nei in adj[c]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

    print("".join(result) if len(result) == 26 else "Impossible")


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

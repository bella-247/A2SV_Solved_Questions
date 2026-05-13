import random, math, sys, heapq
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
    m = ri()

    ops = [rs().split() for _ in range(m)]

    counts = Counter()

    heap = []
    results = []

    for op  in ops:

        match (op[0]):
            case "insert":
                num = int(op[1])
                heappush(heap, num)
                counts[num] += 1
                results.append(f"insert {num}")

            case "removeMin":
                if not heap:
                    results.append("insert 0")
                else:
                    num = heap[0]
                    heappop(heap)
                    counts[num] -= 1
                
                results.append("removeMin")
                
                
            case "getMin":
                num = int(op[1])

                if counts[num] == 0:
                    results.append(f"insert {num}")
                    heappush(heap, num)
                    counts[num] += 1

                while heap[0] != num:
                    results.append("removeMin")
                    x = heap[0]
                    heappop(heap)
                    counts[x] -= 1

                results.append(f"getMin {num}")




    print(len(results))
    for r in results:
        print(r)

def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

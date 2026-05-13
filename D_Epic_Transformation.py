import random, math, sys, heapq as heap
from itertools import accumulate
from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from random import randint
from heapq import heapify, heappush, heappop
import heapq

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
    n = ri()
    nums = rls()
    counts = Counter(nums)
    heap = [[-freq, num] for num, freq in counts.items()]
    heapify(heap)
    print(heap)

    while len(heap) > 1:

        for i in range(1, len(heap)):
            if len(heap) <= 1 or i >= len(heap):
                break

            freq0 = -heap[0][0]
            freqi = -heap[i][0]

            heap[0][0] = -(freq0 + 1)
            heap[i][0] = -(freqi + 1)

            if heap[i][0] == 0:
                heap[i], heap[-1] = heap[-1], heap[i]
                heap.pop()

            if len(heap) >= 1 and heap[0][0] == 0:
                heap[0], heap[-1] = heap[-1], heap[0]
                heap.pop()

            # heapify(heap)

        print(heap)

        if len(heap) < 4:
            break

    print(0 if len(heap) == 0 else -heap[0][0])


def main():
    t = 1
    t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

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
    print("Yes" if res else "No")


def acc(arr):
    return list(accumulate(arr))


rand = random.getrandbits(32)


def xor(x):
    return x ^ rand


# sys.setrecursionlimit(200000) # don't forget to use python 3


def solution(_):
    n, m = rls()

    nums = rls()
    queries = [rls() for _ in range(m)]

    if n == 1:
        return yn(1)

    index_type = []

    for i in range(1, n):
        type = -1 if nums[i - 1] > nums[i] else 0 if nums[i - 1] == nums[i] else 1

        if not index_type or index_type[-1][1] != type:
            index_type.append((i - 1, type))

    ranges = []
    last_2 = -1
    left = 0

    for right in range(len(index_type)):
        if index_type[right][1] == -1:
            last_2 = right

        if index_type[right][1] == 1 and last_2 >= left:
            ranges.append((index_type[left][0], index_type[right][0]))

        while index_type[right][1] == 1 and last_2 >= left:
            left += 1

    ranges.append((index_type[left][0], n - 1))
    mapp = {left: right for left, right in ranges}
    mapp_list = list(mapp.keys())

    for left, right in queries:
        left -= 1
        right -= 1

        index = bisect_right(mapp_list, left) - 1

        if index == -1:
            index = 0

        mapp_left = mapp_list[index]
        mapp_right = mapp[mapp_left]

        yn(mapp_right >= right)


def main():
    t = 1
    # t = ri()
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

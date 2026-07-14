# import random, math, sys, heapq as heap
# from itertools import accumulate
# from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
# from collections import Counter, defaultdict, deque
# from bisect import bisect_left, bisect_right
# from random import randint
# from heapq import heapify, heappush, heappop

# input = sys.stdin.readline


# def print(*args, **kwargs):
#     sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))


# def rs():
#     return input().strip()


# def ri():
#     return int(rs())


# def rls(spliter=" "):
#     return list(map(int, rs().split(spliter)))


# def yn(res):
#     print("YES" if res else "NO")


# def acc(arr):
#     return list(accumulate(arr))


# rand = random.getrandbits(32)


# def xor(x):
#     return x ^ rand


# sys.setrecursionlimit(200000)  # don't forget to use python 3

# INF = 10**18


# def solution(_):
#     n, x, s = rls()
#     chars = list(rs())
#     n = len(chars)

#     seats = 0
#     free = x


# def main():
#     t = 1
#     t = ri()
#     for _ in range(t):
#         solution(_)


# if __name__ == "__main__":
#     main()


#     # memo = {}

#     # def dp(i, occ, free):
#     #     if i == n:
#     #         return 0

#     #     if occ == 0 and free == 0:
#     #         return 0

#     #     tup = (i, occ, free)

#     #     if tup in memo:
#     #         return memo[tup]

#     #     if chars[i] == "I":
#     #         ans = 0
#     #         if free > 0:
#     #             ans = 1 + dp(i + 1, occ + s - 1, free - 1)
#     #         else:
#     #             ans = dp(i + 1, occ, free)

#     #         memo[tup] = ans
#     #         return ans

#     #     if chars[i] == "E":
#     #         ans = 0
#     #         if occ > 0:
#     #             ans = 1 + dp(i + 1, occ - 1, free)
#     #         else:
#     #             ans = dp(i + 1, occ, free)

#     #         memo[tup] = ans
#     #         return ans

#     #     best = 0
#     #     if free > 0:
#     #         best = 1 + dp(i + 1, occ + s - 1, free - 1)

#     #     if occ > 0:
#     #         best = max(best, 1 + dp(i + 1, occ - 1, free))

#     #     memo[tup] = best

#     #     return best

#     # print(dp(0, 0, x))


import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        s = int(data[idx + 2])
        u = data[idx + 3]
        idx += 4

        T = 0
        rem = 0
        ans = 0
        count_A_as_seat = 0

        for char in u:
            # Optimization: If we hit maximum physical venue capacity, stop early
            if ans == x * s:
                break

            if char == "I":
                if T < x:
                    T += 1
                    rem += s - 1
                    ans += 1

            elif char == "E":
                if rem > 0:
                    rem -= 1
                    ans += 1
                elif T < x and count_A_as_seat > 0:
                    # Retroactively convert a past 'A' from taking a seat to opening a table
                    count_A_as_seat -= 1
                    T += 1
                    rem += (
                        s - 1
                    )  # +1 returned seat + (s-1) new seats - 1 seat for current E
                    ans += 1

            elif char == "A":
                if rem > 0:
                    rem -= 1
                    ans += 1
                    count_A_as_seat += 1
                elif T < x:
                    T += 1
                    rem += s - 1
                    ans += 1

        out.append(str(ans))

    print("\n".join(out))


if __name__ == "__main__":
    solve()

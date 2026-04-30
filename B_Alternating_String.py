from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

# sys.setrecursionlimit(200000) # don't forget to use python 3
input = sys.stdin.readline


def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))


def read_int():
    return int(input().strip())


def read_ints():
    return map(int, input().split())


def read_list():
    return list(map(int, input().split()))


def yn(res):
    print("YES" if res else "NO")


inf = float("inf")


# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    s = input().strip()
    nums = [2 * int(s[i] == "a") - 1 for i in range(len(s))]
    n = len(nums)

    k = 4

    window = sum(nums[:k])

    if window == k:
        return yn(0)

    left = 0
    for right in range(k, n):
        window += nums[right]
        window -= nums[left]

        if window >= k:
            return yn(0)

        left += 1

    yn(1)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

# sys.setrecursionlimit(10**7)
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


def get_cbrt(n):
    low = 1
    high = 10**4  # For n up to 10^12, cbrt is 10^4
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        cube = mid * mid * mid
        if cube == n:
            return mid
        elif cube < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


pre_compute = set(i**3 for i in range(1, 10**4))


# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    x = read_int()

    for cube in pre_compute:
        if x - cube in pre_compute:
            return yn(1)

    yn(0)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

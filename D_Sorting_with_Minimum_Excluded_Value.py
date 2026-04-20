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


# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7


def is_sorted(arr):
    return all(arr[i] == i for i in range(len(arr)))


def mex(arr):
    n = len(arr)

    s = set(arr)
    for i in range(n + 1):
        if i not in s:
            return i

    return 0


def solution(_):
    n = read_int()
    nums = read_list()

    not_updated = set(range(n))

    ops = []

    so = is_sorted(nums)

    while not so:
        mx = mex(nums)
        
        index = mx if mx < n else not_updated.pop()
        not_updated.discard(index)
        
        if nums[index] == index:
            continue
        
        ops.append(index + 1)
        nums[index] = mx

        so = is_sorted(nums)

    print(len(ops))
    print(*ops)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

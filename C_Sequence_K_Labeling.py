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
def solution(_):
    n, k = read_ints()

    nums = read_list()

    groups = [[set(), set()] for _ in range(k)]

    for i in range(n):
        inserted = False

        for group in groups:
            if not group[0]:
                group[0].add(nums[i])
                group[1].add(i)
                inserted = True
                break

        j = 0
        while not inserted and j < len(groups):
            group = groups[j]

            if nums[i] not in group[0]:
                group[0].add(nums[i])
                group[1].add(i)
                inserted = True
                break

            j += 1

        if not inserted:
            return yn(0)

    result = [0] * n

    color = 1

    for _, indices in groups:
        for index in indices:
            result[index] = color

        color += 1

    yn(1)
    print(*result)


def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

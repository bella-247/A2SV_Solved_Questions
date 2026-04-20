from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

sys.setrecursionlimit(10**7)
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
    n, m = read_ints()
    nums = read_list()

    al = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        v1, v2 = read_ints()
        al[v1].append(v2)
        al[v2].append(v1)

    def backtrack(vertex, parent, cons_ones):
        if not al[vertex]:
            return 1

        if len(al[vertex]) == 1 and al[vertex][0] == parent:
            return 1

        paths = 0
        for child in al[vertex]:
            if child == parent:
                continue

            index = child - 1

            new_cons_ones = 0 if nums[index] == 0 else cons_ones + 1

            if new_cons_ones > m:
                continue

            paths += backtrack(child, vertex, new_cons_ones)

        return paths

    print(backtrack(1, -1, nums[0]))


def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

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
    a, b = read_ints()
    n = read_int()
    cars = [read_list() for _ in range(n)]

    smallest = inf

    for x, y, s in cars:
        distance = math.sqrt((x - a) ** 2 + (y - b) ** 2)

        smallest = min(smallest, distance / s)

    print(smallest)


def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

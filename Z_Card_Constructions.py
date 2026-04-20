from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

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

pre = [2]
MAX = 10**9 + 10

# use python 3

while pre[-1] < MAX:
    k = len(pre) + 1
    pre.append(pre[-1] + k * 2 + k - 1)



def solution(_):
    n = read_int()

    count = 0

    while n > 1:
        index = bisect.bisect_right(pre, n) - 1

        if index < 0:
            break

        count += 1

        n -= pre[index]

    print(count)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

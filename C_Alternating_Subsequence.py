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
    n = read_int()
    nums = read_list()

    groups = []
    
    for i in range(n):
        if groups and (groups[-1][-1] > 0) == (nums[i] > 0):
            groups[-1].append(nums[i])
        else:
            groups.append([nums[i]])
            
    print(sum(max(group) for group in groups))


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

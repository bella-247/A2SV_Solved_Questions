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
    n, k = read_list()
    nums = read_list()
    nums.sort()

    
    for i in range(n - 2, -1, -2):
        if k == 0:
            break
        
        new = min(nums[i + 1], nums[i] + k)
        add = new - nums[i]
        nums[i] = new
        k -= add
        
    p2 = 0
    for i in range(n - 2, -1, -2):
        p2 += nums[i]
    
    p1 = 0
    for i in range(n - 1, -1, -2):
        p1 += nums[i]

    print(p1 - p2)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

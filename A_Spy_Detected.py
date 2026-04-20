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
    n = read_int()
    nums = read_list()
    
    for i in range(1, n - 1):
        if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            return print(i + 1)
        
        elif nums[i] == nums[i - 1] and nums[i] != nums[i + 1]:
            return print(i + 2)
            
        elif nums[i] == nums[i + 1] and nums[i] != nums[i - 1]:
            return print(i)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)


if __name__ == "__main__":
    main()

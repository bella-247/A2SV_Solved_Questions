from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

# sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("Yes" if res else "No")

inf = float('inf')
MOD = 10**9 + 7
def solution(_):
    parents = defaultdict(list)
    n = read_int()
    nums = [-1, -1] + [int(input()) for _ in range(n - 1)]
    
    for i in range(2, n + 1):
        parents[nums[i]].append(i)
    
    for children in parents.values():
        count = 0
        for child in children:
            if child not in parents:
                count += 1
                
        if count < 3:
            yn(False)
            return
        
    yn(True)


def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
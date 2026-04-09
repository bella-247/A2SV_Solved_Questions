from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools
import random

input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
MOD = 10**9 + 7

def solution(_):
    n = read_int()
    nums = read_list()
    counts = defaultdict(list)
    
    for i in range(n):
        counts[nums[i]].append(i + 1)
        
    
    for num, indices in counts.items():
        if len(indices) < 2:
            print(-1)
            return
        
        k = len(indices)
        for i in range(k):
            nums[indices[i] - 1] = indices[(i + 1) % k]
        
        
    print(*nums)

    




































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
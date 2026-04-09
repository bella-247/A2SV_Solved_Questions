from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

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
    
    for i in range(n - 1):
        if abs(nums[i] - nums[i+1]) <= 1:
            print(0)
            return
        
    for i in range(n - 2):
        left = min(nums[i+1], nums[i+2])
        right = max(nums[i+1], nums[i + 2])
        
        if left - 1 <= nums[i] <= right + 1:
            print(1)
            return
            
    print(-1)
        


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
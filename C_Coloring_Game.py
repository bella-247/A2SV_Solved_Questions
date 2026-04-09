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
    
    nums.sort()
    
    maxx = nums[-1]
    
    count = 0
    
    for k in range(n - 1, 1, -1):
        i, j = 0, k - 1
        
        while j > i:
            while i < j and nums[i] + nums[j] <= nums[k] or nums[i] + nums[j] + nums[k] <= maxx:
                i += 1
            
            if j > i:
                count += (j - i)
                j -= 1
        
    print(count)
 
def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
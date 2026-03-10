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

def minSubK(nums, start, k):
    result = [-1, -1]
    left = start
    n = len(nums)
    window = 0
    for right in range(start, n):
        window += nums[right]
        while window >= k:
            result[:] = [left, right]
            
            window -= nums[left]
            left += 1 
            
            if window - nums[left] < k:
                return result
        
    return result
        

def solution():
    n, m, v = read_ints()
    nums = read_list()
    
    ranges = []
    
    start = -1
    for _ in range(m):
        result = minSubK(nums, start+1, v)
        if result[0] == -1:
            print(-1)
            return
        
        ranges.append(result)
        start = result[1]


    maxx = 0
    start = -1
    for left, right in ranges:
        maxx = max(maxx, sum(nums[start+1:left]))
        start = right
        
    maxx = max(maxx, sum(nums[ranges[-1][1]:]))
    
    print(maxx)

def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()
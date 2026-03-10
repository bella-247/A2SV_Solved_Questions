from collections import defaultdict, deque, Counter
import math
import sys

input = sys.stdin.readline
def spaced(): return list(map(int, input().strip().split()))
def number(): return int(input().strip())


def solution():
    I = lambda x : int(x) - 1
    n = int(input().strip())
    nums = spaced()
    m = int(input().strip())
    
    sorted_nums = sorted(nums)
    nums.append(0)
    sorted_nums.append(0)
    
    for i in range(n):
        nums[i] += nums[i-1]
        sorted_nums[i] += sorted_nums[i-1]
        
    for _ in range(m):
        t, left, right = map(I, input().strip().split())
        
        if t == 0:
            print(nums[right] - nums[left - 1])
            
        else:
            print(sorted_nums[right] - sorted_nums[left -1])
            
    

t = 1
# t = int(input().strip())
for _ in range(t):
    solution()
    
    
    
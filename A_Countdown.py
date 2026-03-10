from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    nums = list(map(int, input().strip()))
    
    total = sum(nums)
    
    for i in range(n-2, -1, -1):
        if nums[i] > 0:
            total += 1
            
    print(total)
    

    

t = 1
t = int(input().strip())
for _ in range(t):
    solution()
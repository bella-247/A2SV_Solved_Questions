from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().strip().split())
    
    nums = list(map(int, input().strip().split()))
    window = sum(nums[:k])
    smallest = window
    start = 1
    
    left = 0
    for right in range(k, n):
        window -= nums[left]
        window += nums[right]
        left += 1
        
        if window < smallest:
            window = smallest
            start = left + 1
        
    print(start)
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

t = 1
# t = int(input().strip())
for _ in range(t):
    solution()
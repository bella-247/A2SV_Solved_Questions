from collections import defaultdict, deque, Counter
import math
import random
import sys
input = sys.stdin.readline

def solution():  
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    longest = 0
    window = Counter()
    result = [1, 1]
    
    left = 0
    
    for right in range(n):
        window[nums[right]] += 1
        
        while len(window) > k:
            window[nums[left]] -= 1
            
            if window[nums[left]] == 0:
                del window[nums[left]]
                
            left += 1
            
        if right - left + 1 > longest:
            longest = right - left + 1
            result = [left + 1, right + 1]        
    
    print(*result)
    
    
t = 1
# t = int(input().strip())
for _ in range(t):
    solution()
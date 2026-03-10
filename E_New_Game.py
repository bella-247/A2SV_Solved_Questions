from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    win_max = 0
    longest = 0
    window = Counter()
    left = 0
    for right in range(n):
        if nums[right] > win_max + 1:
            window = Counter()
            left = right
            
        win_max = max(win_max, nums[right])
        window[nums[right]] += 1
        
        while left <= right and len(window) > k:
            window[nums[left]] -= 1
            
            if window[nums[left]] == 0:
                del window[nums[left]]
                
            left += 1
            
        longest = max(longest, right - left + 1)

    print(longest)

t = 1
t = int(input().strip())
for _ in range(t):
    solution()
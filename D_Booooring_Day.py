from collections import defaultdict, deque, Counter
from itertools import count
import math
import sys
input = sys.stdin.readline

def solution():
    n, l, r = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0
    window = 0
    left = 0
    for right in range(n):
        window += nums[right]
        
        while left <= right and window > r:
             window -= nums[left]
             left += 1
        
        if window == 0:
            left = right + 1
        
        elif l <= window <= r:
            count += 1
            left = right + 1
            window = 0
    
    print(count)
    
t = 1
t = int(input().strip())
for _ in range(t):
    solution()
from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    nums.sort()
    
    score = 0
    for i in range(0, 2 * n, 2):
        score += min(nums[i], nums[i + 1])
        
    print(score)
    
t = 1
t = int(input().strip())
for _ in range(t):
    solution()
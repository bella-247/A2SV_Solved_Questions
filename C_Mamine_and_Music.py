from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    indexed_nums = sorted([num, i] for i, num in enumerate(nums))
    
    window = deque()
    cur_win = deque()
    
    win_sum = 0
    
    left = 0
    for right in range(n):
        num, index = indexed_nums[right]
        win_sum += num
        cur_win.append(index + 1)
        
        while win_sum > k:
            win_sum -= indexed_nums[left][0]
            cur_win.popleft()
            left += 1
            
        if len(cur_win) > len(window):
            window = cur_win.copy()
    
    
    print(len(window))
    print(*window)

    
    

t = 1
# t = int(input().strip())
for _ in range(t):
    solution()
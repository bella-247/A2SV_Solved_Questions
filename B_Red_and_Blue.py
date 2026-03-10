from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    reds = list(map(int, input().strip().split()))
    m = int(input().strip())
    blues = list(map(int, input().strip().split()))
    
    for i in range(1, n):
        reds[i] += reds[i-1]
        
    for i in range(1, m):
        blues[i] += blues[i-1]
    
    largest_red_prefix_sum = max(0, *reds)
    largest_blue_prefix_sum = max(0, *blues)
    
    print(largest_red_prefix_sum + largest_blue_prefix_sum)
    

t = 1
t = int(input().strip())
for _ in range(t):
    solution()


# largest = 0
# for i in range(n):
#     for j in range(m):
#         largest = max(largest, reds[i] + blues[j])
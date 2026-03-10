from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().strip().split())
    nums = [int(input().strip()) for _ in range(n)]
    
    counts = Counter(nums)
    
    count = 0
    for num, freq in list(counts.items()):
        rem = freq % 2
        count += (freq - rem)
        counts[num] = rem
        
        if counts[num] == 0:
            del counts[num]
            
    count += (len(counts) + 1) // 2

    print(count)
    
    

t = 1
# t = int(input().strip())
for _ in range(t):
    solution()
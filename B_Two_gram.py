from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    s = input().strip()
    
    counts = Counter()
    
    for i in range(n-1):
        counts[s[i:i+2]] += 1
        
    print(max(counts, key=lambda x : counts[x]))
    
    
    

t = 1
# t = int(input().strip())
for _ in range(t):
    solution()
from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    s = input().strip()
    
    if len(s) <= 3:
        print("NO")
        return
    
    counts = Counter(s)
    
    doubles = sum(1 for count in counts.values() if count >= 2)
    
    if doubles >= 2:
        print("YES")
        return
    else:
        print("NO")
        return

t = 1
t = int(input().strip())
for _ in range(t):
    solution()
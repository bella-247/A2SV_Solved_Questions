from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    s = input().strip()
    counts = Counter(s)
    k = min(counts["H"], counts["T"])
    swap_char = "H" if counts["H"] > counts["T"] else "T"
    
    s = s + s[:k-1]
    
    window = 0
    for i in range(k):
        if s[i] == swap_char:
            window += 1
            
    minn = window

    left = 0
    for right in range(k, len(s)):
        if s[right] == swap_char:
            window += 1
            
        if s[left] == swap_char:
            window -= 1
    
        left += 1
        minn = min(minn, window)
    
    print(minn)
    
t = 1
# t = int(input().strip())
for _ in range(t):
    solution()
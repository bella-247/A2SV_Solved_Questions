from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    s = input()
    
    window = 0
    for i in range(k):
        if s[i] == "W":
            window += 1
    
    smallest = window
    
    left = 0
    for right in range(k, n):
        if s[right] == "W":
            window += 1
            
        if s[left] == "W":
            window -= 1
        
        left += 1
        smallest = min(smallest, window)
        
    print(smallest)
    return
    

t = 1
t = int(input().strip())
for _ in range(t):
    solution()
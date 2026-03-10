from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    s = list(map(int, input().strip()))
    goal = list(map(int, input().strip()))
    
    flipables = [False] * n
    ones = 0
    zeros = 0
    for i in range(n):  
        if s[i] == 0:
            zeros += 1
        else:
            ones += 1
            
        if zeros == ones:
            flipables[i] = True
            
    flips = 0
    for i in range(n-1, -1, -1):
        # based on the flips, (if odd flip it, else leave it)
        if flips % 2 == 1:
            s[i] = 1 - s[i]
        
        if s[i] != goal[i]:
            if not flipables[i]:
                print("NO")
                return
            else:
                flips += 1
            
    print("YES")
    

t = 1
t = int(input().strip())
for _ in range(t):
    solution()
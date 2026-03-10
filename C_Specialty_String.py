from collections import Counter, defaultdict
import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    s = list(input().strip())
    
    if n % 2 != 0:
        print("NO")
        return
    
    stack = []
    
    for i in range(n):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    
    print("NO" if stack else "YES")

t = 1
t = int(input().strip())
for _ in range(t):
    solution()
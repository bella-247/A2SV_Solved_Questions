from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
MOD = 10**9 + 7

def solution(_):
    n = read_int()
    s = list(input().strip())
    
    stack = []
    
    for i in range(n):
        if stack and stack[-1] == s[i]:
            if len(stack) % 2 == 0:
                stack.append(s[i])
                
        else:
            stack.append(s[i])
    
    if len(stack) % 2 != 0:
        stack.pop()
    
    print(n - len(stack))
    print("".join(stack))
    

def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
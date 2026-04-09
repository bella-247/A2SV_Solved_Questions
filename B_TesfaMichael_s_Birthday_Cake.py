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
    n, k = read_ints()
    s = sorted(input().strip())
    
    for i in range(n):
        stack = []
        j = 0
        while j < n and len(stack) < k:
            if not stack or ord(s[j]) - ord(stack[-1]) > 1:
                stack.append(s[j])
                
            j += 1
                
            
        if len(stack) == k:
            total = 0
            for char in stack:
                total += (ord(char) - ord("a") + 1)
            
            print(total)
            return
        
    print(-1)


def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
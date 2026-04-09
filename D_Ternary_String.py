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
    s = input().strip()
    n = len(s)


    if n < 3:
        print(0)
        return 
    
    shortest = float("inf")
    window = Counter()
    
    left = 0
    for right in range(n):
        window[s[right]] += 1
        
        while len(window) == 3:
            shortest = min(shortest, right - left + 1)
            window[s[left]] -= 1
            
            if window[s[left]] == 0:
                del window[s[left]]
                
            left += 1
            
    if shortest == float("inf"):
        print(0)
    else:
        print(shortest)
        











def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
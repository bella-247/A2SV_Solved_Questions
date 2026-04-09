from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

# sys.setrecursionlimit(10**7)
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
    s = input().strip()
    
    mid = (n - 1) // 2
    char = s[mid]
    
    longest = 0
    
    left = mid
    right = mid + (n + 1) % 2
    
    while left >= 0 and right <= n - 1:
        if s[left] == char:
            longest = right - left + 1
            
        else:
            break
        
        left -= 1
        right += 1
            
    print(longest)
    return 























def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
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
def solution():
    n, k = read_ints()
    s = input().strip()
    
    prefix = [0] * n
    prefix[0] = int(s[0])

    for i in range(1, n):
        prefix[i] = prefix[i-1] + int(s[i])
    
    suffix = [0] * n
    suffix[-1] = int(s[-1])
    
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] + int(s[i])
    
    prefix.append(0)
    suffix.append(0)
    
    total = 0
    
    i = 0
    while i < n:
        if s[i] == "1":
            i += k + 1
            continue
        
        left = max(0, i - k)
        right = min(n-1, i + k)
        
        left_range_count = prefix[i] - prefix[left - 1]
        right_range_count = suffix[i] - suffix[right + 1]

        if max(left_range_count, right_range_count) == 0:
            total += 1
            i += k
            
        i += 1
    
    print(total)
    

def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()
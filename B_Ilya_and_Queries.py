from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().strip().split())
def read_list(): return list(map(int, input().strip().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
MOD = 10**9 + 7

def solution():
    s = input().strip()
    m = read_int()
    n = len(s)
    
    prefix = [0] * (n + 1)
    
    for i in range(n-1):
        prefix[i + 1] = prefix[i]
        
        if s[i] == s[i+1]:
            prefix[i+1] += 1
    
    for _ in range(m):
        left, right = read_ints()
        left -= 1
        right -= 1
        
        print(prefix[right] - prefix[left])


def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()
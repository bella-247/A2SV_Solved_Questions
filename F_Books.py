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
    n, t = read_ints()
    nums = read_list()

    longest = 0
    window = 0
    
    left = 0
    for right in range(n):
        window += nums[right]
        
        while window > t:
            window -= nums[left]
            left += 1
            
        longest = max(longest, right - left + 1)
        
    print(longest)
    

def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
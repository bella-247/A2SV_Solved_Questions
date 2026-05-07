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
    perms = read_list()
    nums = read_list()
    
    indices = [-1] * (n + 1)
    
    for i, num in enumerate(perms):
        indices[num] = i
        
    for i in range(n-1):
        if indices[nums[i]] > indices[nums[i + 1]]:
            return yn(0)
        
    yn(1)
        
    
        



def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
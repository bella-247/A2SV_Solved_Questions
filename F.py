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

def PREFIX(arr):
    n = len(arr)
    prefix = 0
    for i in range(n):
        if arr[i] == "T":
            prefix += 1
            
        else:
            prefix -= 1
            
            if prefix < 0:
                return False
            
    return True
            

def solution(_):
    n = read_int()
    s = list(input().strip())
    
    counts = Counter(s)
    
    yn(counts["T"] == counts["M"] * 2 and  PREFIX(s) and PREFIX(s[::-1]))
    
    
def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
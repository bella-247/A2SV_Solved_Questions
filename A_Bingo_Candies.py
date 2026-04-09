from collections import defaultdict, deque, Counter
import math
import random
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

rand = random.randint(1, 1000000)

inf = float('inf')
MOD = 10**9 + 7
def solution(_):
    n = read_int()
    grid = [read_list() for _ in range(n)]
    counts = Counter()
    
    for i in range(n):
        for j in range(n):
            counts[grid[i][j] ^ rand] += 1
            
            
    maxx = max(counts.values())

    limit = n * n - n
    
    if n == 1:
       yn(False)
       return 
   
    if n == 2:
        yn(not maxx >= 3)
        return
    
    yn(not maxx > limit)
        



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
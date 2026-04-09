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

inf = float('inf')
MOD = 10**9 + 7
def solution(_):
    n, m = read_ints()
    grid = [read_list() for _ in range(n)]
    
    
    
    
    if n == 1 and m == 1:
        print(-1)
        return
    
    grid.reverse()
    
    if len(grid) % 2 != 0:
        grid[n // 2], grid[0] = grid[0], grid[n // 2]
    
    for row in grid:
        row.reverse()
        k = len(row)
        
        if len(row) % 2 != 0:
            row[0], row[k // 2] = row[k // 2], row[0] 
            
    
    for row in grid:
        print(*row)
 


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline

def spaced(): 
    return list(map(int, input().strip().split()))
def unspaced():
    return list(input().strip())

def F(char):
    return 1 if char == "." else 0
    
def solution():
    I = lambda x : int(x) - 1
    h, w = spaced()
    grid = [unspaced() for _ in range(h)]
    q = int(input().strip())
    
    grid.append(["#"] * w)
    for row in grid:
        row.append("#")
    
    left_prefix = [[0] * (w + 1) for _ in range(h + 1)]
    top_prefix = [[0] * (w + 1) for _ in range(h + 1)]
    
    for i in range(h):
        for j in range(w):
            if F(grid[i][j]):
                left_prefix[i][j] = F(grid[i][j-1]) 
                top_prefix[i][j] = F(grid[i-1][j])


    for i in range(h):
        for j in range(w):
            left_prefix[i][j] = left_prefix[i][j] + left_prefix[i-1][j] + left_prefix[i][j-1] - left_prefix[i-1][j-1]
            top_prefix[i][j] = top_prefix[i][j] + top_prefix[i-1][j] + top_prefix[i][j-1] - top_prefix[i-1][j-1]
            
    
    for _ in range(q):
        r1, c1, r2, c2 = map(I, input().strip().split())
        result = top_prefix[r2][c2] - top_prefix[r2][c1-1] - top_prefix[r1][c2] + top_prefix[r1][c1-1]
        result += left_prefix[r2][c2] - left_prefix[r1-1][c2] - left_prefix[r2][c1] + left_prefix[r1-1][c1]
        
        print(result)
        



t = 1
# t = int(input().strip())
for _ in range(t):
    solution()

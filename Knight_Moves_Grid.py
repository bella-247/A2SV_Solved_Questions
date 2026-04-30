# import random, math, sys, heapq as heap
# from itertools import accumulate
# from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
# from collections import Counter, defaultdict, deque
# from bisect import bisect_left, bisect_right
# from random import randint

# input = sys.stdin.readline


# def print(*args, **kwargs):
#     sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))


# def rs():
#     return input().strip()


# def ri():
#     return int(rs())


# def rls(spliter=" "):
#     return list(map(int, rs().split(spliter)))


# def yn(res):
#     print("Yes" if res else "No")


# def acc(arr):
#     return list(accumulate(arr))


# rand = random.getrandbits(32)


# def xor(x):
#     return x ^ rand


# # sys.setrecursionlimit(200000) # don't forget to use python 3

# output = []


# def solution(_):
#     n = ri()

#     grid = [[-1 for _ in range(n)] for _ in range(n)]

#     def in_bound(row, col):
#         return -1 < row < n and -1 < col < n

#     directions = [
#         (-2, -1),
#         (-1, -2),
#         (1, -2),
#         (2, -1),
#         (-2, 1),
#         (-1, 2),
#         (1, 2),
#         (2, 1),
#     ]

#     queue = deque([[0, 0]])

#     steps = 0
#     while queue:

#         for i in range(len(queue)):
#             row, col = queue.popleft()

#             grid[row][col] = steps

#             for dr, dc in directions:
#                 nr, nc = row + dr, col + dc

#                 if in_bound(nr, nc) and grid[nr][nc] == -1:
#                     queue.append([nr, nc])

#         steps += 1

#     # Instead of printing in the loop:
#     for row in grid:
#         output.append(" ".join(map(str, row)))


# def main():
#     t = 1
#     # t = ri()
#     for _ in range(t):
#         solution(_)
#     sys.stdout.write("\n".join(output) + "\n")


# if __name__ == "__main__":
#     main()


import sys
from collections import deque

def solve():
    line = sys.stdin.readline()
    if not line: return
    n = int(line.strip())

    # 1D array is faster than 2D array in Python
    dist = [-1] * (n * n)
    dist[0] = 0
    
    queue = deque([0]) # Store flattened index
    
    # Pre-calculate offsets to avoid math inside the loop
    # Moves: (dr, dc) mapped to 1D offset: dr * n + dc
    offsets = []
    for dr, dc in [(-2,-1),(-1,-2),(1,-2),(2,-1),(-2,1),(-1,2),(1,2),(2,1)]:
        offsets.append((dr, dc, dr * n + dc))

    while queue:
        curr_idx = queue.popleft()
        d = dist[curr_idx]
        
        r, c = divmod(curr_idx, n)
        
        for dr, dc, offset in offsets:
            nr, nc = r + dr, c + dc
            ni = curr_idx + offset
            
            if 0 <= nr < n and 0 <= nc < n and dist[ni] == -1:
                dist[ni] = d + 1
                queue.append(ni)

    # Fast Block Output
    
    out = sys.stdout
    for r in range(n):
        out.write(" ".join(map(str, dist[r*n : (r+1)*n])) + "\n")

solve()
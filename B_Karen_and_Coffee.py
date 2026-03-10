from collections import defaultdict, deque, Counter
import math
import sys
input = sys.stdin.readline
def spaced(): return list(map(int, input().strip().split()))
def number(): return int(input().strip())

def solution():
    n, k, q = spaced()
    N = 2 * 10**5 + 2
    
    recipes = [spaced() for _ in range(n)]
    queries = [spaced() for _ in range(q)]

    prefix = [0] * N
    
    for left, right in recipes:
        prefix[left] += 1
        prefix[right + 1] -= 1
        
    for i in range(1, N):
        prefix[i] += prefix[i - 1]
    
    count = 0
    for i in range(1, N):
        if prefix[i] >= k:
            count += 1
        prefix[i] = count
    
    prefix[N - 1] = 0
    
    for left, right in queries:
        print(prefix[right] - prefix[left-1])
    


t = 1
# t = int(input().strip())
for _ in range(t):
    solution()
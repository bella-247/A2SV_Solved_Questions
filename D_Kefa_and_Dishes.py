from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

# sys.setrecursionlimit(200000) # don't forget to use python 3
input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    n, m, k = read_ints()
    satisfactions = read_list()
    
    rels = [[] for _ in range(n + 1)]
    
    for _ in range(k):
        x, y, s = read_list()
        rels[x].append((y, s))
    
    largest = 0
    eaten = set()
    
    def dfs(index, sats):
        nonlocal largest
        if len(eaten) == m:
            largest = max(largest, sats)
        
        
        for cand, sat in rels[index]:
            if cand in eaten:
                continue
            
            idx = cand - 1
            
            
            
            
        



    dfs(0, 0)




def main():
    t = 1
  # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
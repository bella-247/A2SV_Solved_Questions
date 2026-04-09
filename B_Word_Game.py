from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

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
    p1 = set(input().strip().split())
    p2 = set(input().strip().split())
    p3 = set(input().strip().split())
    
    scores = [0] * 3
    
    for word in p1:
        if word in p2 and word in p3:
            continue
        
        elif word in p2:
            scores[0] += 1
            
        elif word in p3:
            scores[0] += 1
            
        else:
            scores[0] += 3
            
    for word in p2:
        if word in p1 and word in p3:
            continue
        
        elif word in p1:
            scores[1] += 1
        elif word in p3:
            scores[1] += 1
            
        else:
            scores[1] += 3
            
    for word in p3:
        if word in p1 and word in p2:
            continue
        
        elif word in p2:
            scores[2] += 1
            
        elif word in p1:
            scores[2] += 1
            
        else:
            scores[2] += 3
            
    print(*scores)


































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
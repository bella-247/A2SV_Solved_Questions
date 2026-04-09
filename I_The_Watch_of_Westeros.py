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
    sweep = Counter()
    
    for i in range(n):
        left, right = read_ints()
        
        sweep[left] += 1
        sweep[right + 1] -= 1
        
    sorted_sweep = sorted(sweep)
    
    m = len(sorted_sweep)
    
    prefix = 0
    for i in range(m):
        num = sorted_sweep[i]
        prefix += sweep[num]
        sweep[num] = prefix
    
    result = Counter()
    
    for i in range(m - 1):
        left = sorted_sweep[i] 
        right = sorted_sweep[i + 1]
        
        freq = sweep[left]
        
        result[freq] += (right - left)

    
    for i in range(1, n+1):
        print(result[i], end=" ")
    




def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
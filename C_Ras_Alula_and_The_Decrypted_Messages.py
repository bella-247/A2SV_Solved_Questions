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
# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    n, m = read_ints()
    D = lambda c: ord(c) - ord("a")
    
    s = input().strip()
    w = input().strip()
    
    target = sum(D(c) for c in w)

    window = sum(D(c) for c in s[:m])
    
    if window == target:
        return yn(1)
    
    left = 0
    for right in range(m, n):
        
        window += D(s[right])
        window -= D(s[left])
        left += 1

        if window == target:
            return yn(1)
        
    yn(0)
        
        
        


































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
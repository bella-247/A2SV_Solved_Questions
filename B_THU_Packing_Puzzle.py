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
    t, h, u = read_ints()
    total = 0
    
    tu = min(t, u)
    t = t - tu
    u = u - tu
    
    total += (tu * 4)
    
    tht = min(t // 2, h)
    h = h - tht
    t = t - (2 * tht)
    
    total += (tht * 7)
        
    th = min(t, h)
    t -= th
    h -= th

    total += (th * 5)
    
    if t > 0:
        total += (3*t - t + 1)
    
    total += (u * 3) + (h * 3)
    
    print(total)
    
    



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
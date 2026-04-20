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
    boys = read_list()
    girls = read_list()
    
    boys.sort()
    girls.sort()
    
    if girls[0] < boys[-1]:
        return print(-1)
    
    maxx = boys[-1]
    
    count = 0
    total = 0
    for i in range(1, m):
        diff = girls[i] - maxx
        total += diff
        count += (diff > 0)
    
    diff = girls[0] - maxx
    
    if count == m - 1 and diff > 0:
        total += girls[0] - boys[-2]
    
    total += sum(boys) * m
    
    print(total)
    
    
    
    



































def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
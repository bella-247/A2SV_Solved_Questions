from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

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
    # don't forget to use python 3

    def rec(n, m):
        if n == m:
            return True
        
        if n < m:
            return False

        if n % 3 != 0:
            return False
        
        x = n // 3
        
        return rec(x,m) or rec(2 * x, m)
        
    
    yn(rec(n, m))

def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
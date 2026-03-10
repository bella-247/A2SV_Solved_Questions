from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
MOD = 10**9 + 7

EVEN = lambda x : False if not x else int(x) % 2 == 0
def isEBNE(n):
    if not n:
        return False
    
    odds = sum(int(c) % 2 for c in n)
    
    return int(n) % 2 != 0 and odds % 2 == 0
    
def solution():
    n = read_int()
    s = list(input().strip())
    
    if isEBNE("".join(s)):
        print(int("".join(s)))
        return
    
    while EVEN("".join(s)):
        s.pop()
        
    odds = sum(int(c) % 2 for c in s)
    i = 0
    while odds % 2 != 0:
        if not EVEN(s[i]):
            odds -= 1
            s.pop(i)
        
        i += 1
        

    if not isEBNE("".join(s)):
        print(-1)
        return
    
    
    print(int("".join(s)))
    return


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()
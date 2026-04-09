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
def solution(_):
    a, b = read_ints()

    def rec(a, b):
        if a == b:
            return [b]
        
        if b < a:
            return []
        
        if b % 2 != 0 and b % 10 != 1:
            return []
        
        if b % 10 == 1:
            return rec(a, b // 10) + [b]
            
        return rec(a, b // 2) + [b]
    
    result = rec(a, b)
    
    if result and result[0] == a and result[-1] == b:
        print("YES")
        print(len(result))
        print(*result)
        
    else:
        print("NO")



































def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
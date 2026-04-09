from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

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
    arr = read_list()
    __ = read_list()
    
    count = 0
    
    for i in range(n):
        
        if i > 0 and math.gcd(arr[i], arr[i-1]) == arr[i]:
            continue
        
        if i < n - 1 and math.gcd(arr[i], arr[i+1]) == arr[i]:
            continue

        count += 1

    print(count)
        



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
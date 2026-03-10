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
def solution():
    n, q = read_ints()
    a = read_list()
    b = read_list()
    
    maxx = max(a[-1], b[-1])
    for i in range(n-1, -1, -1):
        maxx = max(maxx, a[i], b[i])
        
        a[i] = maxx

    prefix = list(itertools.accumulate(a))
    prefix.append(0)
    
    for i in range(q):
        left, right = read_ints()
        left -= 1
        right -= 1
        
        print(prefix[right] - prefix[left-1], end=" ")
        
    print()


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()
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
    a = read_int()
    b = read_int()
    c = read_int()
    
    res1 = max(a + b, a * b)
    res1 = max(res1 + c, res1 * c)

    res2 = max(b + c, b * c)
    res2 = max(res2 + a , res2 * a)
    
    print(max(res1, res2))



































def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
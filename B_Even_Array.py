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
    n = read_int()
    nums = read_list()
    mismatches = 0
    odds = 0
    evens = 0
    
    for i in range(n):
        if i % 2 != nums[i] % 2:
            mismatches += 1
            
            if nums[i] % 2 == 0:
                evens += 1
            else:
                odds += 1
            
    if mismatches % 2 != 0 or odds != evens:
        print(-1)
        return
    
    else:
        print(mismatches // 2)
        return


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()
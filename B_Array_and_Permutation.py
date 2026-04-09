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
    perms = read_list()
    nums = read_list()
    
    indices = {perm : i for i, perm in enumerate(perms)}
    
    for i in range(1, n):
        if indices[nums[i]] < indices[nums[i - 1]]:
            print("NO")
            return
        
    print("YES")



def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
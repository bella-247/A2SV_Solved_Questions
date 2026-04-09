from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

sys.setrecursionlimit(10**7)
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
    
    
    # use python3 
    
    
    n = read_int()
    nums = read_list()
    
    total = sum(nums)
    smallest = float("inf")
    
    def dfs(index, left):
        nonlocal smallest
        if index == n:
            smallest = min(smallest, abs(left - (total - left)))
            return
        
        dfs(index + 1, left)
        dfs(index + 1, left + nums[index])
        
        
    dfs(0, 0)
    print(smallest)




def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
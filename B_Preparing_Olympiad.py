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
    n, l, r, x = read_ints()
    nums = read_list()
    count = 0
    
    def dfs(start, summ, minn, maxx):
        nonlocal count
        
        if l <= summ <= r:
            if maxx - minn >= x:
                count += 1
        
        if summ > r:
            return
        
        for i in range(start, n):
            dfs(i + 1, summ + nums[i], min(minn, nums[i]), max(maxx, nums[i]))
    
    
    dfs(0, 0, inf, -inf)
    
    print(count)
    return



def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
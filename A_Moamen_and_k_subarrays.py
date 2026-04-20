from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

# sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("Yes" if res else "No")

inf = float('inf')
# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    
    n, k = read_list()
    nums = read_list()
    
    sorted_nums = sorted(nums)
    mapp = {num : i for i, num in enumerate(sorted_nums)}
    
    subs = 0
    
    for i in range(n-1):
        if mapp[nums[i]] + 1 != mapp[nums[i + 1]]:
            subs += 1
    
    yn(subs < k)
        
    
































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
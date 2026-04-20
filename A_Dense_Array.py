from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools

# sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
# iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    
    n = read_int()
    nums = read_list()
    
    count = 0
    
    for i in range(n-1):
        maxx = (max(nums[i], nums[i + 1]) + 1) // 2
        minn = min(nums[i], nums[i + 1])
        
        while maxx > minn:
            count += 1
            maxx = (maxx + 1) // 2
            
            
    
    print(count)



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
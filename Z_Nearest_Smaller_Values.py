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
    nearest = [0] * n
    
    stack = []
    
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
            
        if stack:
            nearest[i] = stack[-1] + 1
        
        stack.append(i)
            
            
    print(*nearest)
    
     



































def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
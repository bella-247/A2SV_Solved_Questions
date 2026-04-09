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
MOD = 10**9 + 7
def solution(_):
    n, m = read_ints()
    nums = read_list()
    usables = read_list()
    b = usables[0]
    
    nums[-1] = max(b - nums[-1], nums[-1])
    
    for i in range(n - 1):
        if nums[i] > nums[i + 1] and b - nums[i] > nums[i + 1]:
            yn(0)
            return
        
        if b - nums[i] <= nums[i + 1] and nums[i] <= nums[i + 1]:
            nums[i] = max(nums[i], b - nums[i])
        else:
            nums[i] = min(nums[i], b - nums[i])

    
    for i in range(n-1):
        if nums[i] > nums[i + 1]:
            yn(0)
            return

    yn(1)
    
    



def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
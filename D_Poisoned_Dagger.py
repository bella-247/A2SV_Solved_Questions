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
    n, h = read_ints()
    nums = read_list()
    nums.sort()
    
    max_gap = 0
    goal = h
    
    i = 0
    while i < n-1 and goal > 0:
        gap = nums[i+1] - nums[i]
        max_gap = max(max_gap, gap)        
        goal -= gap
        i += 1
        
    goal -= 1
    max_gap = max(max_gap, goal)
    
    def checker(k):
        goal = h
        nums.append(nums[-1] + k)
        n = len(nums)
        i = 0
        while i < n - 1 and goal > 0:
            gap = nums[i+1] - nums[i]
            damage = min(gap, k)
            goal -= damage
            i += 1

        nums.pop()
        return goal <= 0
    
    left = 1
    right = max_gap
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if checker(mid):
            right = mid - 1
            
        else:
            left = mid + 1
            
    print(left)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
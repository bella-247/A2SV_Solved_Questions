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
iinf = 10 ** 18
# MOD = 10**9 + 7

def solution(_):
    n, m = read_ints()
    nums = read_list()
    nums.append(iinf)
    
    usables = read_list()
    usables.sort()
    
    def search(value, limit):
        left = 0
        right = m - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if usables[mid] - value > limit:
                right = mid - 1
            else:
                left = mid + 1
                
        return usables[right] - value
        
        
    
    for i in range(n - 1, -1, -1):
        value = nums[i]
        search_result = search(value, nums[i + 1])
        
        minn = min(value, search_result)
        maxx = max(value, search_result)
        
        if minn > nums[i + 1]:
            return yn(0)
        
        if maxx <= nums[i + 1]:
            nums[i] = maxx
            
        else:
            nums[i] = minn
    
    
    yn(1)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
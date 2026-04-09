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
    n, k = read_ints()
    nums = read_list()
    counts = [0] * (n+1)
    
    for num in nums:
        counts[num] += 1
        
    for i in range(1, n + 1):
        if counts[i] % k != 0:
            return print(0)
        
        counts[i] //= k
        
    total = 0
        
    window = [0] * (n + 1)
    left = 0
    
    for right, num in enumerate(nums):
        window[num] += 1
        
        while window[num] > counts[num]:
            window[nums[left]] -= 1
            left += 1 
    
        total += (right - left + 1)
        

    print(total)
            
    





def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
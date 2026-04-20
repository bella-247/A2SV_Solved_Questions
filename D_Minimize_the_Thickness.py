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

    smallest = n
    
    for size in range(1, n + 1):        
        target = sum(nums[:size])
        window = 0
    
        largest = 0
        
        left = 0

        for right in range(n):
            window += nums[right]
            
            largest = max(largest, right - left + 1)
            
            if window == target:
                if right == n - 1:
                    smallest = min(smallest, largest)
                    
                else:
                    left = right + 1
                    window = 0
                    
            elif window > target:
                window = 0
                break
            
    print(smallest)
            
                
            
            
    
    
    
    
    
    
    
    



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
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
    n, k  = read_ints()
    
    def calc(num): 
        rest = n - num
        summ = ((num * (num + 1)) // 2)
        return summ - rest
    
    left = 0
    right = n-1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if calc(mid) >= k:
            right = mid - 1
        else:
            left = mid + 1
            
            
    print(n - left)
        
        
        
        
    
    
    
    
    



































def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
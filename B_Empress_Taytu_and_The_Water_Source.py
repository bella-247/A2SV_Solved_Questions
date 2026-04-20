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
iinf = 10 ** 18 + 1
# MOD = 10**9 + 7
def solution(_):
    n, k = read_ints()
    
    needs = read_list()
    times = read_list()
    
    
    def checker(size):
        time = 0
        
        for i in range(n):
            trips = math.ceil(needs[i] / size)
            time += (trips * times[i])
            
        return time <= k
    
    left = 1
    right = iinf 
    
    while left <= right:
        
        mid = left + (right - left) // 2
        
        if checker(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    if checker(left):
        print(left)
    else:
        print(-1)



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
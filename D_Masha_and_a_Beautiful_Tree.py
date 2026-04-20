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
    
    ops = 0
    
    def mergeSort(arr):
        nonlocal  ops
        
        if len(arr) == 1:
            return arr

        mid = (len(arr) - 1) // 2
        
        left = mergeSort(arr[:mid + 1])
        right = mergeSort(arr[mid + 1: ])
        
        if left[0] > right[0]:
            ops += 1
            
            return right + left

        return left + right
            
    result = mergeSort(nums)
    
    for i in range(n-1):
        if result[i] > result[i + 1]:
            return print(-1)
        
    
    print(ops)
    
    



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
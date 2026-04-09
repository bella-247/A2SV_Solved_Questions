from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

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

def mergeSort(arr):
    if len(arr) == 1:
        return arr, 0
    
    n = len(arr)
    mid = n // 2
    
    left, left_count = mergeSort(arr[:mid])
    right, right_count = mergeSort(arr[mid:])
    
    cur_count = 0
    for end in left:
        cur_count += bisect.bisect_right(right, end)
    
    return sorted(left + right), (cur_count + left_count + right_count)


def solution(_):
    n = read_int()
    ranges = [read_list() for _ in range(n)]
    ranges.sort()
    
    ends = [end for _, end in ranges]
    
    __, count = mergeSort(ends)
    
    print(count)
        
    

def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
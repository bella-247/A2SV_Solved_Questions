from collections import defaultdict, deque, Counter
import math
from operator import index
import sys
import bisect
import itertools

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
    n = read_int()
    nums = read_list()
    
    indices = defaultdict(list)
    
    for i, num in enumerate(nums):
        indices[num].append(i)

    
    for index_list in indices.values():
        for i in range(1, len(index_list)):
            if index_list[-1] - index_list[0] > 1:
                print("YES")
                return
            
        
    print("NO")
    
    



































def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
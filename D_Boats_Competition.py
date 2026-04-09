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
def solution(_):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    max_teams = 0
    
    for target in range(2, 2*n + 1):
        teams = 0
        
        i = 0
        j = n - 1
        
        while i < j:
            summ = nums[i] + nums[j]
            
            if summ == target:
                teams += 1
                i += 1
                j -= 1
                
            elif summ > target:
                j -= 1
                
            else:
                i += 1
            
        max_teams = max(max_teams, teams)
    
    print(max_teams)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
from collections import defaultdict, deque, Counter
import math
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
    n, m, v = read_ints()
    nums = read_list()
    prefix = list(itertools.accumulate(nums))
    prefix.append(0)
    
    ending_positions = [-1]
    starting_positions = []
    
    cur_sum = 0
    for i in range(n):
        cur_sum += nums[i]
        
        if cur_sum >= v:
            ending_positions.append(i)
            cur_sum = 0
            
        if len(starting_positions) == m:
            break
        
    cur_sum = 0
    for i in range(n-1, -1, -1):
        cur_sum += nums[i]
        
        if cur_sum >= v:
            starting_positions.append(i)
            cur_sum = 0
            
        if len(starting_positions) == m:
            break
        
    starting_positions.reverse()
    starting_positions.append(n)
    
    if len(ending_positions) < m  + 1:
        print(-1)
        return
    
    maxx = 0
    
    for i in range(m + 1):
        alice_start = ending_positions[i] + 1
        alice_end = starting_positions[i]
        
        cur_sum = prefix[alice_end-1] - prefix[alice_start-1]
        maxx = max(cur_sum, maxx)
        
    print(maxx)
    

def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
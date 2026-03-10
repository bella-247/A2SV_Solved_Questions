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

def solution():
    n, b = read_ints()
    nums = read_list()
    
    points = []
    
    odds = 0
    evens = 0
    
    for i in range(n-1):
        if nums[i] % 2 == 0:
            evens += 1
        else:
            odds += 1
            
        if odds == evens:
            points.append(i)
    
    points.sort(key=lambda i: abs(nums[i] - nums[i+1]))
    
    cuts = 0
    cost = 0
    
    for index in points:
        newCost = abs(nums[index] - nums[index + 1])
        
        if cost + newCost > b:
            break
            
        cost += newCost
        cuts += 1

    print(cuts)
    return













def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()
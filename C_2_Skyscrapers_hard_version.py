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
INF = 10 ** 18
MOD = 10**9 + 7

def previousSmaller(nums):
    pre_smaller = defaultdict(lambda : -1)
    
    stack = []
    
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] >= num:
            stack.pop()
            
        if stack:
            pre_smaller[i] = stack[-1]
            
        stack.append(i)
        
    return pre_smaller

def solution(_):
    n = read_int()
    limits = read_list()
    preSmaller = previousSmaller(limits)
    
    prefix = [0] * n
    
    for i in range(n):
        pre_index = preSmaller[i]
        pre_value = prefix[pre_index] if pre_index != -1 else 0
        upto_value = limits[i] * (i - pre_index)
        
        prefix[i] = pre_value + upto_value
    

    reversed_limits = limits[::-1]
    
    preSmaller = previousSmaller(reversed_limits)
    suffix = [0] * n
    
    for i in range(n):
        pre_index = preSmaller[i]
        pre_value = suffix[pre_index] if pre_index != -1 else 0
        upto_value = reversed_limits[i] * (i - pre_index)
        
        suffix[i] = pre_value + upto_value
        
    
    # reverse to get the real suffix
    suffix.reverse()
    
    
    peak_index = 0
    
    for i in range(n):
        peak_index = max(peak_index, i, key= lambda index : prefix[index] + suffix[index] - limits[index])
        
    
    result = [0] * n
    limit = limits[peak_index]
    
    for i in range(peak_index, -1, -1):
        limit = min(limit, limits[i])
        result[i] = limit
        
    limit = limits[peak_index]
    
    for i in range(peak_index, n):
        limit = min(limit, limits[i])
        result[i] = limit
    
    
    print(*result)
    

def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
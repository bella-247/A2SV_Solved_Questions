from collections import defaultdict, deque, Counter
import itertools
import math
import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    
    odds = sum(num % 2 for num in nums)

    if odds < k:
        print("NO")
        return
    
    if (odds - k) % 2 != 0:
        print("NO")
        return

    result = []
    prefix = list(itertools.accumulate(nums))
    remainder = 1
    i = 0
    m = k
    while m > 1 and i < n:
        if prefix[i] % 2 == remainder:
            result.append(i + 1)
            remainder = 1 - remainder
            m -= 1
            
        i += 1
    
    # find the last index
    end = -1
    while i < n:
        if prefix[i] % 2 == remainder:
            end = (i + 1)
            
        i += 1
        
    if end != -1:
        result.append(end)
        
    if len(result) != k:
        print("NO")
        return
    
    print("YES")
    print(*result)
    
t = 1
t = int(input().strip())
for _ in range(t):
    solution()
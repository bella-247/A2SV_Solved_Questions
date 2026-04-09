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
    n, k = read_ints()
    nums = read_list()
    
    min_deque = deque()
    max_deque = deque()

    result = []
    
    longest = 0
    
    left = 0
    for right in range(n):
        
        while min_deque and nums[min_deque[-1]] > nums[right]:
            min_deque.pop()
            
        min_deque.append(right)
        
        while max_deque and nums[max_deque[-1]] < nums[right]:
            max_deque.pop()
            
        max_deque.append(right)
        
        while min_deque and max_deque and nums[max_deque[0]] - nums[min_deque[0]] > k:
            if max_deque[0] == left:
                max_deque.popleft()
                
            if min_deque[0] == left:
                min_deque.popleft()
                
            left += 1
            
            
        longest = max(longest, right - left + 1)
        
        result.append([left, right])


    answer = []
    for left , right in result:
        if right - left + 1 == longest:
            answer.append([left + 1, right + 1])

    print(longest, len(answer))
    for ans in answer:
        print(*ans)
    
    
    
def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()
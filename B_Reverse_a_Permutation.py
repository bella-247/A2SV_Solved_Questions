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
    n = read_int()
    nums = read_list()

    indices = {num : i for i, num in enumerate(nums)}

    left = 0
    num = n
    
    while left < n and nums[left] == num:
        left += 1
        num -= 1
    
    if num in indices:
        right = indices[num]
        
        j = right
        mid = (left + right) // 2
        for i in range(left, mid + 1):
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        # nums[left : right + 1] = nums[left:right+1][::-1]
    
    print(*nums)















def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()
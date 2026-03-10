import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    
    maxx = max(nums)
    
    print(nums.count(maxx))
    

t = 1
t = int(input().strip())
for _ in range(t):
    solution()
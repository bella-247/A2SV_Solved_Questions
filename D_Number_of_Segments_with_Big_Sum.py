import sys
input = sys.stdin.readline

def solve():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))

    count = 0
    
    window = 0
    left = 0
    for right in range(n):
        window += nums[right]
        
        while left <= right and window >= s:
            count += (n - right)
            window -= nums[left]
            left += 1
            
    print(count)
    return

t = 1
# t = int(input())
for _ in range(t):
    solve()

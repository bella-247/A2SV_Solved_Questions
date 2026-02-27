n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))

shortest = float("inf")

cur_sum = 0
left = 0

for right in range(n):
    cur_sum += nums[right]
    
    while cur_sum >= s:
        shortest = min(shortest, right - left + 1)
        cur_sum -= nums[left]
        left += 1
        
print(shortest if shortest < float("inf") else -1)

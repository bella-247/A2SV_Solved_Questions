n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))

longest = 0

cur_sum = 0
left = 0
for right in range(n):
    cur_sum += nums[right]
    while cur_sum > s:
        cur_sum -= nums[left]
        left += 1
        
    longest = max(longest, right - left + 1)

print(longest)

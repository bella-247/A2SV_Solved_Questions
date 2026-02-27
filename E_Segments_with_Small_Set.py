from collections import Counter

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

count = 0

window = Counter()
left = 0

for right in range(n):
    window[nums[right]] += 1

    while len(window) > k:
        window[nums[left]] -= 1
        
        if window[nums[left]] == 0:
            del window[nums[left]]
        
        left += 1
        
    count += (right - left + 1)
    
print(count)
    
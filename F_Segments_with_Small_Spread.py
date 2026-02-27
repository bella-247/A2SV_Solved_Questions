from collections import deque

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
count = 0

maxDeque = deque()
minDeque = deque()

left = 0
for right in range(n):
    while maxDeque and nums[maxDeque[-1]] < nums[right]:
        maxDeque.pop()
    maxDeque.append(right)
        
    while minDeque and nums[minDeque[-1]] > nums[right]:
        minDeque.pop()
    minDeque.append(right)
    
    while maxDeque and minDeque and nums[maxDeque[0]] - nums[minDeque[0]] > k:
        if maxDeque[0] == left:
            maxDeque.popleft()
            
        if minDeque[0] == left:
            minDeque.popleft()
            
        left += 1
    
    count += (right - left + 1)

print(count)


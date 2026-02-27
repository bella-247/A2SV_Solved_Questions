n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

gaps = [ nums[i] - nums[i-1] for i in range(1, n)]

gaps.sort(reverse=True)

print(sum(gaps[k-1:]))
    
    

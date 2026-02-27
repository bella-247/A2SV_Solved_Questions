for _ in range(int(input())):
    n = int(input())
    
    nums = list(map(int, input().split()))
    result = [nums[0]]
    for i in range(1, n - 1):
        if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
            result.append(nums[i])
            
        if nums[i - 1] > nums[i] and nums[i + 1] > nums[i]:
            result.append(nums[i])
            
    result.append(nums[-1])
    
    print(len(result))   
    print(*result)
    
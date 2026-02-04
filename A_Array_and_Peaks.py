t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    nums = list(range(1, n + 1))
    
    if k > 0 and (n - 1) // k < 2:
        print(-1)
        continue
    
    for i in range(k):
        index = 2 * i + 1
        nums[index], nums[index + 1] = nums[index + 1], nums[index]
        
    for num in nums:
        print(num, end = " ")
        
    print()
    
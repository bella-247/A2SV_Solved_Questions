for _ in range(int(input())):
    n = int(input())
    
    nums = list(map(int, input().split()))
    count = 0
    
    i = 0
    while i < n - 1:
        x, y = nums[i], nums[i + 1]
        
        if x == y or x == 7 - y:
            count += 1
            i += 1
            
        i += 1
            
    print(count)
def yes_no(check):
    print("YES" if check else "NO")
    
for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    
    for i in range(1, n + 1):
        num = i
        
        if nums[i] == num:
            continue
        
        double_index = 2 * i
        
        while double_index <= n:
            if nums[double_index] == num:
                break
            double_index *= 2
            
        else:
            yes_no(False)
            break
                        
        
        while double_index != i:
            half = double_index // 2
            nums[double_index], nums[half] = nums[half], nums[double_index]
            double_index = half
            
    else:
        yes_no(True)
    
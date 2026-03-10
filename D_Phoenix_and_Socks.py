from collections import Counter
for _ in range(int(input())):
    n, l, r = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    left, right = arr[:l], arr[l:]
    
    if l < r:
        left, right = right, left
        l, r = r, l
    
    left_counts = Counter(left)
    right_counts = Counter(right)
    
    op_count = 0
    
    required_transfer = (l - r) // 2
    op_count = required_transfer
    
    # balancing
    for num in left_counts:
        if required_transfer == 0:
            break
        
        if left_counts[num] <= right_counts[num]:
            continue
        
        transfer = (left_counts[num] - right_counts[num]) // 2
        transfer = min(required_transfer, transfer)
        
        left_counts[num] -= transfer
        right_counts[num] += transfer
        
        required_transfer -= transfer
        
    
    for num in left_counts:
        minn = min(left_counts[num], right_counts[num])
        left_counts[num] -= minn
        right_counts[num] -= minn
    
    left_count_sum = sum(left_counts.values())
    right_count_sum = sum(right_counts.values())
    
    color_changes = (left_count_sum + right_count_sum) // 2    
    op_count += color_changes
    
    print(op_count)


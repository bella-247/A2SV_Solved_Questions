import sys
sys.stdin.read().split()

def flippingBinary(n, nums):
    ones_indices = []
    zeros_indices = []
    
    for i in range(n):
        if nums[i] == "1":
            ones_indices.append(i + 1)
            
        else:
            zeros_indices.append(i + 1)
            
    ones = len(ones_indices)
    zeros = n - ones
    
    if ones % 2 == 0:
        return ones, ones_indices
    
    if zeros % 2 != 0:
        return zeros, zeros_indices
    
    return -1, []

for _ in range(int(input())):
    n = int(input())
    nums = input()
    
    operations, indices = flippingBinary(n, nums)
    
    print(operations)
    if operations > 0:
        print(*indices)
    
    
    
    
    
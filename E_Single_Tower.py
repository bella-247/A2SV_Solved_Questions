n = int(input())
towers = [] 
nums = []
for i in range(n):
    k, *blocks = list(map(int, input().split()))
    towers.append(blocks)
    nums.extend(blocks)

nums.sort()
mapp = {nums[i] : i for i in range(len(nums))}

splits = 0

for blocks in towers:
    for i in range(1, len(blocks)):
        block = blocks[i]
        prev_block = blocks[i - 1]
        
        if mapp[block] != mapp[prev_block] + 1:
            splits += 1
            
combinations = n + splits - 1
print(splits, combinations)    

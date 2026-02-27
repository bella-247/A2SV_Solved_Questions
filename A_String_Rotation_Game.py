def stringRotation(s, n):
    max_block_size = 0
    blocks = 0
    
    cur = s[0]
    i = 0
    while i < n:
        count = 0
        blocks += 1
        while i < n and s[i] == cur:
            count += 1
            i += 1
            
        if i != n:
            cur = s[i]
            
        max_block_size = max(max_block_size, count)
    
    if max_block_size == 1 or s[0] == s[-1]:
        return blocks
    
    if s[0] != s[-1]:
        return blocks + 1


for _ in range(int(input())):
    n = int(input())
    s = input()
    
    print(stringRotation(s, n))
    
    

        
        

    
            
        
    